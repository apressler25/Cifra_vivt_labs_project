from fastapi import APIRouter, Depends
from schemas.home_shcema import (HomeResponseSchema,LasttrainSchema)
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select
from models.models_bd import ( TrainInfo, TrainPool,  ProgramsWorkout, 
                            WorkoutExercises,ApproachesRec, WorkoutExPool)
from sqlalchemy import func, extract
from datetime import  date

homerouter = APIRouter(prefix="/home", tags=["ГЛАВНЫЙ ЭКРАН"])
    
@homerouter.get("/{telegram_id}", name="Домашняя страница", response_model=HomeResponseSchema)
async def get_mainpage(telegram_id: int, session: AsyncSession = Depends(get_async_session)):
    today = date.today()
    
    russian_days = {
        0: 'Понедельник',  # Monday
        1: 'Вторник',      # Tuesday
        2: 'Среда',        # Wednesday
        3: 'Четверг',      # Thursday
        4: 'Пятница',      # Friday
        5: 'Суббота',      # Saturday
        6: 'Воскресенье'   # Sunday
    }
    today_russian = russian_days[today.weekday()]

    # 1. Проверка есть ли сегодня тренировка в программе
    today_train_query = (
        select(func.count(ProgramsWorkout.id_programs_workout))
        .where(
            ProgramsWorkout.id_user == telegram_id,
            ProgramsWorkout.week_day_programs_workout == today_russian
        )
    )
    today_train_count = await session.scalar(today_train_query)
    check_train_this_day = today_train_count > 0

    # 2. Тренировался ли сегодня пользователь (была ли запись о тренировке сегодня)
    today_trained_query = (
        select(func.count(TrainInfo.id_train_info))
        .where(
            TrainInfo.Id_user == telegram_id,
            func.date(TrainInfo.datetime_start_train_info) == today
        )
    )
    today_trained_count = await session.scalar(today_trained_query)
    check_train_this_day_any_ready = today_trained_count > 0

    # 3. Название программы на сегодня (если есть)
    program_for_today_name = None
    if check_train_this_day:
        program_name_query = (
            select(ProgramsWorkout.name_programs_workout)
            .where(
                ProgramsWorkout.id_user == telegram_id,
                ProgramsWorkout.week_day_programs_workout == today_russian
            )
            .limit(1)
        )
        program_for_today_name = await session.scalar(program_name_query)

    # 4. Программа тренировки на сегодня пустая?
    if check_train_this_day:
        # Проверяем есть ли связанные записи в Workout_ex_pool для программ на сегодня
        workout_ex_pool_count_query = (
            select(func.count(WorkoutExPool.id_ex_pool))
            .join(ProgramsWorkout, WorkoutExPool.id_programs_workout == ProgramsWorkout.id_programs_workout)
            .where(
                ProgramsWorkout.id_user == telegram_id,
                ProgramsWorkout.week_day_programs_workout == today_russian
            )
        )
        workout_ex_pool_count = await session.scalar(workout_ex_pool_count_query) or 0
        program_for_today_is_empty = workout_ex_pool_count == 0
    else:
        program_for_today_is_empty = False

    # 5. Всего тренировок пользователя
    count_train_query = (
        select(func.count(TrainInfo.id_train_info))
        .where(TrainInfo.Id_user == telegram_id)
    )
    count_train_user = await session.scalar(count_train_query) or 0

    # 6. Общее время всех тренировок в формате "1 ч 30 мин"
    total_time_query = (
        select(
            func.sum(
                extract('epoch', TrainInfo.datetime_end_train_info - TrainInfo.datetime_start_train_info)
            )
        )
        .where(
            TrainInfo.Id_user == telegram_id,
            TrainInfo.datetime_end_train_info.isnot(None)
        )
    )
    total_seconds = await session.scalar(total_time_query) or 0

    # Конвертируем секунды в часы и минуты
    if total_seconds > 0:
        total_minutes = int(total_seconds // 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        max_time_train = f"{hours} ч {minutes} мин"
    else:
        max_time_train = "0 ч 0 мин"

    # 7. Упражнение с рекордом по весу и сам вес
    record_train_query = (
        select(
            WorkoutExercises.name_workout_exercises,
            func.max(ApproachesRec.weight_approaches_rec).label('max_weight')
        )
        .join(TrainPool, ApproachesRec.id_train_pool == TrainPool.id_train_pool)
        .join(WorkoutExercises, TrainPool.id_workout_exercises == WorkoutExercises.id_workout_exercises)
        .join(TrainInfo, TrainPool.id_train_info == TrainInfo.id_train_info)
        .where(TrainInfo.Id_user == telegram_id)
        .group_by(WorkoutExercises.name_workout_exercises)
        .order_by(func.max(ApproachesRec.weight_approaches_rec).desc())
    )
    record_train_result = await session.execute(record_train_query)
    record_train_data = record_train_result.all()

    record_train_info = []
    for exercise in record_train_data:
        exercise_name = exercise[0]
        max_weight = exercise[1]
        
        record_train_info.append(
            LasttrainSchema(
                last_train_name_ex=exercise_name,
                last_train_result_ex=f"{max_weight} кг"
            )
        )

    # 8. Количество программ пользователя
    program_count_query = (
        select(func.count(ProgramsWorkout.id_programs_workout))
        .where(ProgramsWorkout.id_user == telegram_id)
    )
    program_user_name_count = await session.scalar(program_count_query) or 0

    # 9. Данные последней тренировки
    last_train_query = (
        select(
            TrainInfo.id_train_info,
            TrainInfo.datetime_start_train_info
        )
        .where(TrainInfo.Id_user == telegram_id)
        .order_by(TrainInfo.datetime_start_train_info.desc())
        .limit(1)
    )
    last_train_info = await session.execute(last_train_query)
    last_train_data = last_train_info.first()

    last_train_exercises = []
    if last_train_data:
        last_train_id = last_train_data[0]
        
        # Получаем упражнения из последней тренировки с группировкой по упражнениям
        last_exercises_query = (
            select(
                WorkoutExercises.name_workout_exercises,
                func.max(ApproachesRec.weight_approaches_rec).label('max_weight'),
                func.max(ApproachesRec.num_iteration_approaches_rec).label('max_iterations')
            )
            .select_from(TrainPool)
            .join(WorkoutExercises, TrainPool.id_workout_exercises == WorkoutExercises.id_workout_exercises)
            .join(ApproachesRec, TrainPool.id_train_pool == ApproachesRec.id_train_pool)
            .where(TrainPool.id_train_info == last_train_id)
            .group_by(WorkoutExercises.name_workout_exercises)
        )
        last_exercises_result = await session.execute(last_exercises_query)
        last_exercises = last_exercises_result.all()
        
        for ex in last_exercises:
            exercise_name = ex[0]
            max_weight = ex[1]
            max_iterations = ex[2]
            result_str = f"{max_weight}кг × {max_iterations}"
            
            last_train_exercises.append(
                LasttrainSchema(
                    last_train_name_ex=exercise_name,
                    last_train_result_ex=result_str
                )
            )

    return HomeResponseSchema(
        check_train_this_day=check_train_this_day,
        check_train_this_day_any_ready=check_train_this_day_any_ready,
        program_for_today_is_empty=program_for_today_is_empty,
        program_for_today_name=program_for_today_name,
        count_train_user=count_train_user,
        max_time_train=max_time_train,
        record_train_info=record_train_info,
        program_user_name_count=program_user_name_count,
        last_train_ex=last_train_exercises
    )