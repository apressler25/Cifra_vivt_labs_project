
from fastapi import APIRouter, Depends, HTTPException
from schemas.hystory_workout_schema import (WorkoutDatesResponse, AllWorkoutsResponse, 
                                            WorkoutDetailResponse, ExerciseResult, WorkoutSet, WorkoutSummary)
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select

from models.models_bd import ( TrainInfo, TrainPool,  
                            WorkoutExercises,TargetMuscleCategory,ApproachesRec)

from datetime import datetime, timedelta
from schemas.user_schemas import StatusResponse
from sqlalchemy import exists


hystory_workout_router = APIRouter(prefix="/hystory", tags=["ИСТОРИЯ ТРЕНИРОВОК"])


#Получение списка всех созданных упражнений у конкретного пользователя
@hystory_workout_router.get('/dates/{user_id}', summary="Получение дат тренировок за последние 3 месяца", response_model=WorkoutDatesResponse)
async def get_workout_dates(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        three_months_ago = datetime.now() - timedelta(days=90)
        
        dates_query = (
            select(TrainInfo.datetime_start_train_info)
            .where(
                TrainInfo.Id_user == user_id,
                TrainInfo.datetime_start_train_info >= three_months_ago
            )
            .order_by(TrainInfo.datetime_start_train_info)
        )
        
        dates_result = await session.execute(dates_query)
        dates = dates_result.scalars().all()
        
        # Удаляем дубликаты дат (если несколько тренировок в один день)
        unique_dates = set()
        formatted_dates = []
        
        for date in dates:
            date_str = date.strftime("%d.%m.%Y")
            if date_str not in unique_dates:
                unique_dates.add(date_str)
                formatted_dates.append(date_str)
        
        return WorkoutDatesResponse(dates=formatted_dates)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении дат тренировок: {str(e)}")
    


@hystory_workout_router.get("/workouts/{user_id}", 
                            response_model=AllWorkoutsResponse, 
                            summary="Получение всех тренировок пользователя")
async def get_workout_summary(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Получение сводки всех тренировок пользователя
    
    Args:
        user_id: ID пользователя (telegram_id)
        
    Returns:
        Список тренировок с основной информацией
    """
    try:
        # Получаем все тренировки пользователя
        workouts_query = (
            select(
                TrainInfo.id_train_info,  # workout_id
                TrainInfo.name_programs_workout,  # workout_name
                TrainInfo.datetime_start_train_info,  # date и start_time
                TrainInfo.datetime_end_train_info  # end_time
            )
            .where(TrainInfo.Id_user == user_id)
            .order_by(TrainInfo.datetime_start_train_info.desc())
        )
        
        workouts_result = await session.execute(workouts_query)
        workoutsq = workouts_result.all()
        
        workout_summaries = []
        
        for workout in workoutsq:
            workout_id = workout[0]  # id_train_info
            workout_name = workout[1]  # name_programs_workout
            start_datetime = workout[2]  # datetime_start_train_info
            end_datetime = workout[3]  # datetime_end_train_info
            
            # Проверяем есть ли прогресс (record_bool = True в Train_pool)
            progress_query = (
                select(exists().where(
                    TrainPool.id_train_info == workout_id,
                    TrainPool.record_bool == True
                ))
            )
            progress_result = await session.execute(progress_query)
            has_progress = progress_result.scalar()
            
            # Форматируем дату в "20 июля"
            date_str = start_datetime.strftime("%d %B").replace(
                "January", "января").replace("February", "февраля").replace(
                "March", "марта").replace("April", "апреля").replace(
                "May", "мая").replace("June", "июня").replace(
                "July", "июля").replace("August", "августа").replace(
                "September", "сентября").replace("October", "октября").replace(
                "November", "ноября").replace("December", "декабря")
            
            # Форматируем время начала в "HH:MM"
            start_time_str = start_datetime.strftime("%H:%M")
            
            # Форматируем время завершения в "HH:MM" (если есть)
            end_time_str = end_datetime.strftime("%H:%M") if end_datetime else "—"
            
            workout_summaries.append(
                WorkoutSummary(
                    workout_name=workout_name,  # name_programs_workout из таблицы Train_info
                    workout_id=workout_id,  # id_train_info из таблицы Train_info
                    date=date_str,  # Дата в формате "20 июля" из datetime_start_train_info таблицы Train_info
                    start_time=start_time_str,  # Время начала в формате "HH:MM" из datetime_start_train_info таблицы Train_info
                    end_time=end_time_str,  # Время завершения в формате "HH:MM" из datetime_end_train_info таблицы Train_info
                    has_progress=bool(has_progress)  # если у хотя бы у одного связанного элемента из таблицы Train_pool есть True в поле record_bool, ставится True, в ином случае - False
                )
            )
        
        return AllWorkoutsResponse(workouts=workout_summaries)
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Ошибка при получении сводки тренировок: {str(e)}"
        )
        


@hystory_workout_router.get("/details/{workout_id}", 
                            response_model=WorkoutDetailResponse, 
                            summary="Получение детальной информации по тренировке")
async def get_workout_detail(
    workout_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Получение детальной информации о конкретной тренировке
    
    Args:
        workout_id: ID тренировки (id_train_info)
        
    Returns:
        Детальная информация о тренировке
    """
    try:
        # Получаем основную информацию о тренировке
        workout_query = (
            select(
                TrainInfo.name_programs_workout,
                TrainInfo.datetime_start_train_info,
                TrainInfo.datetime_end_train_info
            )
            .where(TrainInfo.id_train_info == workout_id)
        )
        
        workout_result = await session.execute(workout_query)
        workout_data = workout_result.first()
        
        if not workout_data:
            raise HTTPException(status_code=404, detail="Тренировка не найдена")
        
        workout_name, start_datetime, end_datetime = workout_data
        
        # Форматируем дату и время
        workout_date = start_datetime.strftime("%d.%m.%Y")
        
        if end_datetime:
            workout_time = f"{start_datetime.strftime('%H:%M')} - {end_datetime.strftime('%H:%M')}"
            duration_seconds = (end_datetime - start_datetime).total_seconds()
            hours = int(duration_seconds // 3600)
            minutes = int((duration_seconds % 3600) // 60)
            duration = f"{hours}ч {minutes}мин" if hours > 0 else f"{minutes}мин"
        else:
            workout_time = f"{start_datetime.strftime('%H:%M')} - —"
            duration = "—"
        
        # Получаем все упражнения тренировки с подходами
        exercises_query = (
            select(
                WorkoutExercises.name_workout_exercises,
                TargetMuscleCategory.name_muscle_category,
                ApproachesRec.id_approaches_rec,
                ApproachesRec.weight_approaches_rec,
                ApproachesRec.num_iteration_approaches_rec,
                ApproachesRec.rest_time_up_approaches_rec,
                ApproachesRec.rest_time_down_approaches_rec,
                ApproachesRec.record_bool,
                TrainPool.record_bool.label('train_pool_record_bool')
            )
            .select_from(TrainPool)
            .join(WorkoutExercises, TrainPool.id_workout_exercises == WorkoutExercises.id_workout_exercises)
            .join(TargetMuscleCategory, WorkoutExercises.id_muscle_category == TargetMuscleCategory.id_muscle_category)
            .join(ApproachesRec, TrainPool.id_train_pool == ApproachesRec.id_train_pool)
            .where(TrainPool.id_train_info == workout_id)
            .order_by(
                TrainPool.id_train_pool,
                ApproachesRec.id_approaches_rec
            )
        )
        
        exercises_result = await session.execute(exercises_query)
        exercises_data = exercises_result.all()
        
        # Группируем данные по упражнениям
        exercises_dict = {}
        total_volume = 0.0
        
        for row in exercises_data:
            exercise_name = row[0]
            muscle_group = row[1]
            
            if exercise_name not in exercises_dict:
                exercises_dict[exercise_name] = {
                    'muscle_group': muscle_group,
                    'sets': [],
                    'total_rest_seconds': 0,
                    'set_count': 0
                }
            
            # Рассчитываем отдых для подхода
            rest_seconds = 0
            if row[5] and row[6]:  # rest_time_up и rest_time_down
                rest_seconds = (row[5] - row[6]).total_seconds()
                exercises_dict[exercise_name]['total_rest_seconds'] += rest_seconds
            
            # Добавляем подход
            set_number = len(exercises_dict[exercise_name]['sets']) + 1
            exercises_dict[exercise_name]['sets'].append(
                WorkoutSet(
                    set_number=set_number,
                    weight=float(row[3]),
                    repetitions=row[4],
                    has_progress=row[7] or row[8]  # record_bool из ApproachesRec или TrainPool
                )
            )
            exercises_dict[exercise_name]['set_count'] += 1
            
            # Добавляем к общему объему
            total_volume += float(row[3]) * row[4]
        
        # Формируем список упражнений
        exercises_list = []
        for exercise_name, exercise_data in exercises_dict.items():
            average_rest = 0
            if exercise_data['set_count'] > 0:
                average_rest = int(exercise_data['total_rest_seconds'] / exercise_data['set_count'])
            
            exercises_list.append(
                ExerciseResult(
                    exercise_name=exercise_name,
                    target_muscle_group=exercise_data['muscle_group'],
                    sets=exercise_data['sets'],
                    average_rest=average_rest
                )
            )
        
        return WorkoutDetailResponse(
            workout_name=workout_name,
            workout_date=workout_date,
            workout_time=workout_time,
            duration=duration,
            volume=total_volume,
            exercises=exercises_list
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Ошибка при получении детальной информации о тренировке: {str(e)}"
        )


# class ExerciseResult(BaseModel): представляет собой таблицу Train_pool
#     exercise_name: str  # Название упражнения name_workout_exercises из таблицы Workout_exercises
#     target_muscle_group: str  # Целевая группа мышц name_muscle_category из таблицы Target_muscle_category
#     sets: List[WorkoutSet]  # Список подходов
#     average_rest: int  # Средний отдых в секундах - находится по разнице rest_time_up_approaches_rec и rest_time_down_approaches_rec деленной на количество всех подходов
    
# class WorkoutSet(BaseModel): представляет собой таблицу Approaches_rec
#     set_number: int  # Номер подхода считается для каждого подхода сортировкой по возрастанию id_approaches_rec и начинается с 1, для каждого упражнения начинается заново
#     weight: float  # Рабочий вес - вес использовавшийся в подходе weight_approaches_rec
#     repetitions: int  # Количество повторений num_iteration_approaches_rec
#     has_progress: bool  # Был ли прогресс record_bool
    


# class WorkoutDetailResponse(BaseModel):
#     workout_name: str  # Название тренировки - name_programs_workout в таблице Train_info
#     workout_date: str  # Дата тренировки в формате "дд.мм.гг" из datetime_start_train_info в таблице Train_info
#     workout_time: str  # Время тренировки в формате "18:30 - 19:37" считается из datetime_start_train_info и datetime_end_train_info в таблице Train_info
#     duration: str  # Длительность тренировки (например, "1ч 7мин") считается из datetime_start_train_info и datetime_end_train_info в таблице Train_info
#     volume: float  # Объем тренировки сумма веса сумма всех весов каждого подхода (weight_approaches_rec * num_iteration_approaches_rec) внутри тренировки 
#     exercises: List[ExerciseResult]  # Список результатов по упражнениям