
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select

from models.models_bd import ( TrainInfo, TrainPool, WorkoutExPool, ProgramsWorkout, 
                            WorkoutExercises, ApproachesRec)
from sqlalchemy.orm import selectinload
from sqlalchemy import func, and_
from datetime import datetime
from schemas.user_schemas import StatusResponse
from schemas.session_workout_schema import (CreateWorkoutRequest, ApproachesWithExercise, 
                                            TakeInfoTrainPoolWithExercise, TakeInfoTrainInfoWithExercises, 
                                            TakeInfoTrainPoolWithExerciseUpdate, ApproachesWithExerciseUpdate)


session_workout_router = APIRouter(prefix="/workout-session", tags=["ВЕДЕНИЕ ТРЕНИРОВКИ"])


@session_workout_router.post("/start", summary="Создание тренировки", response_model=StatusResponse)
async def create_workout(
    request: CreateWorkoutRequest,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        # Получаем текущий день недели на русском
        weekdays_ru = {
            0: "понедельник",
            1: "вторник", 
            2: "среда",
            3: "четверг",
            4: "пятница",
            5: "суббота",
            6: "воскресенье"
        }
        today_weekday = weekdays_ru[datetime.now().weekday()]
        
        # Проверяем, есть ли у пользователя тренировка на сегодня
        stmt_program = select(ProgramsWorkout).where(
            and_(
                ProgramsWorkout.id_user == request.user_id,
                func.lower(ProgramsWorkout.week_day_programs_workout) == today_weekday
            )
        )
        result_program = await session.execute(stmt_program)
        program = result_program.scalar_one_or_none()
        
        if not program:
            return StatusResponse(
                status=False,
                message="На сегодня нет запланированной тренировки"
            )
        
        # Проверяем, нет ли уже активной тренировки у пользователя
        stmt_active_train = select(TrainInfo).where(
            and_(
                TrainInfo.Id_user == request.user_id,
                TrainInfo.datetime_end_train_info == None,
                TrainInfo.check_train_info == False
            )
        )
        result_active_train = await session.execute(stmt_active_train)
        active_train = result_active_train.scalar_one_or_none()
        
        if active_train:
            return StatusResponse(
                status=False,
                message="У вас уже есть активная тренировка. Завершите ее перед началом новой."
            )
        
        # Создаем запись в Train_info
        new_train_info = TrainInfo(
            datetime_start_train_info=datetime.now(),
            datetime_end_train_info=None,
            check_train_info=False,
            Id_user=request.user_id,
            name_programs_workout=program.name_programs_workout,
            record_bool=False
        )
        
        session.add(new_train_info)
        await session.flush()  # Получаем id_train_info
        
        # Сохраняем ID созданной тренировки
        train_info_id = new_train_info.id_train_info
        
        # Получаем все упражнения для этой программы
        stmt_ex_pool = select(WorkoutExPool).where(
            WorkoutExPool.id_programs_workout == program.id_programs_workout
        )
        result_ex_pool = await session.execute(stmt_ex_pool)
        workout_exercises = result_ex_pool.scalars().all()
        
        if not workout_exercises:
            return StatusResponse(
                status=False,
                message="В программе тренировки нет упражнений"
            )
        
        # Создаем записи в Train_pool и Approaches_rec
        exercises_count = 0
        approaches_count = 0
        
        for workout_ex in workout_exercises:
            # Создаем запись в Train_pool
            new_train_pool = TrainPool(
                id_train_info=train_info_id,
                record_bool=False,
                id_workout_exercises=workout_ex.id_workout_exercises
            )
            
            session.add(new_train_pool)
            await session.flush()  # Получаем id_train_pool
            
            # Создаем подходы в Approaches_rec
            for approach_num in range(workout_ex.approaches_target_ex_pool):
                new_approach = ApproachesRec(
                    weight_approaches_rec=0,
                    rest_time_up_approaches_rec=None,
                    rest_time_down_approaches_rec=None,
                    num_iteration_approaches_rec=0,
                    id_train_pool=new_train_pool.id_train_pool,
                    record_bool=False
                )
                session.add(new_approach)
                approaches_count += 1
            
            exercises_count += 1
        
        # Фиксируем все изменения
        await session.commit()
        
        return StatusResponse(
            status=True,
            message=f"Тренировка '{program.name_programs_workout}' успешно создана",
            data={
                "train_info_id": train_info_id,
                "exercises_count": exercises_count,
                "approaches_count": approaches_count,
                "program_name": program.name_programs_workout
            }
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при создании тренировки: {str(e)}"
        )
        

# Расширенный GET запрос
@session_workout_router.get("/exercises/{workout_history_id}", 
                        summary="Получение упражнений для ведения тренировки",
                        response_model=TakeInfoTrainInfoWithExercises)
async def get_detailed_workout_info(
    train_info_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        # Получаем Train_info с связанными данными, включая информацию об упражнениях и мышечных группах
        stmt = (
            select(TrainInfo)
            .options(
                selectinload(TrainInfo.train_pools)
                .selectinload(TrainPool.approaches_records),
                selectinload(TrainInfo.train_pools)
                .selectinload(TrainPool.workout_exercise)
                .selectinload(WorkoutExercises.muscle_category)
            )
            .where(TrainInfo.id_train_info == train_info_id)
        )
        
        result = await session.execute(stmt)
        train_info = result.scalar_one_or_none()
        
        if not train_info:
            return StatusResponse(
            status=False,
            message=f"Тренировка не найдена: {str(e)}")
        
        # Формируем список упражнений с подходами
        examples_train = []
        
        for train_pool in train_info.train_pools:
            # Формируем список подходов для текущего упражнения
            completed_sets = []
            for approach in train_pool.approaches_records:
                approach_data = ApproachesWithExercise(
                    working_weight=approach.weight_approaches_rec,
                    rest_start_time=approach.rest_time_up_approaches_rec,
                    rest_end_time=approach.rest_time_down_approaches_rec,
                    repetitions=approach.num_iteration_approaches_rec,
                    set_id=approach.id_approaches_rec
                )
                completed_sets.append(approach_data)
            
            # Получаем информацию о мышечной группе
            muscle_category = train_pool.workout_exercise.muscle_category
            
            # Создаем объект TrainPool с подходами и информацией об упражнении
            train_pool_data = TakeInfoTrainPoolWithExercise(
                exercise_name=train_pool.workout_exercise.name_workout_exercises,
                exercise_history_id=train_pool.id_train_pool,
                target_muscle_group_id=muscle_category.id_muscle_category if muscle_category else 0,
                target_muscle_group_name=muscle_category.name_muscle_category if muscle_category else "Не указана",
                description=train_pool.workout_exercise.notice_workout_exercises or "",
                completed_sets=completed_sets
            )
            examples_train.append(train_pool_data)
        
        # Создаем финальный объект ответа
        response_data = TakeInfoTrainInfoWithExercises(
            workout_name=train_info.name_programs_workout,
            exercises=examples_train
        )
        
        return response_data
        
    except HTTPException:
        raise
    except Exception as e:
        return StatusResponse(
            status=False,
            message=f"Ошибка при получении информации о тренировке: {str(e)}")
        
# TakeInfoTrainPoolWithExerciseUpdate, ApproachesWithExerciseUpdate
@session_workout_router.put('/update_exercise/{exercise_history_id}', summary='Обновление истории по упражнению', response_model=StatusResponse)
async def update_workoutex(exercise_history_id:int, new_workoutex_data:TakeInfoTrainPoolWithExerciseUpdate, session: AsyncSession=Depends(get_async_session)):
    
    try:
        # Получаем TrainPool с связанными подходами
        stmt = (
            select(TrainPool)
            .options(
                selectinload(TrainPool.approaches_records)
            )
            .where(TrainPool.id_train_pool == exercise_history_id)
        )
        
        result = await session.execute(stmt)
        train_pool = result.scalar_one_or_none()
        
        if not train_pool:
            return StatusResponse(
                status=False,
                message="Упражнение не найдено"
            )
        
        # Обновляем record_bool для TrainPool если передано
        if new_workoutex_data.was_record is not None:
            train_pool.record_bool = new_workoutex_data.was_record
        
        # Создаем словарь для быстрого доступа к подходам по ID
        approaches_dict = {approach.id_approaches_rec: approach for approach in train_pool.approaches_records}
        
                # Функция для преобразования datetime
        def fix_datetime_for_db(dt):
            """Преобразует aware datetime в naive datetime для базы данных"""
            if dt is not None and dt.tzinfo is not None:
                return dt.replace(tzinfo=None)
            return dt
        
        # Обновляем подходы
        for approach_update in new_workoutex_data.completed_sets:
            approach = approaches_dict.get(approach_update.set_id)
            
            if not approach:
                return StatusResponse(
                    status=False,
                    message=f"Подход с ID {approach_update.set_id} не найден в этом упражнении"
                )
            
            # Обновляем поля подхода если они переданы
            if approach_update.working_weight is not None:
                approach.weight_approaches_rec = approach_update.working_weight
            
            if approach_update.repetitions is not None:
                approach.num_iteration_approaches_rec = approach_update.repetitions
            
            if approach_update.rest_start_time is not None:
                approach.rest_time_up_approaches_rec = fix_datetime_for_db(approach_update.rest_start_time)
            
            if approach_update.rest_end_time is not None:
                approach.rest_time_down_approaches_rec = fix_datetime_for_db(approach_update.rest_end_time)
            
            if approach_update.was_record is not None:
                approach.record_bool = approach_update.was_record
        
        # Сохраняем изменения
        await session.commit()
        
        return StatusResponse(
            status=True,
            message="Данные упражнения и подходов успешно обновлены",
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при обновлении данных упражнения: {str(e)}"
        )


from services.all_service import delete_zero_iteration_approaches
@session_workout_router.put("/complete/{workout_history_id}", response_model=StatusResponse, 
                            summary="Завершение тренировки")
async def complete_workout(
    workout_history_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        
        # Получаем Train_info по ID
        stmt = select(TrainInfo).where(TrainInfo.id_train_info == workout_history_id)
        result = await session.execute(stmt)
        train_info = result.scalar_one_or_none()
        
        if not train_info:
            return StatusResponse(
                status=False,
                message="Тренировка не найдена"
            )
        
        # Проверяем, не завершена ли уже тренировка
        if train_info.check_train_info:
            return StatusResponse(
                status=False,
                message="Тренировка уже завершена"
            )
        delete_zero_iteration_approaches(train_info.Id_user, session)
        
        # Устанавливаем check_train_info в True
        train_info.check_train_info = True
        
        # Опционально: устанавливаем datetime_end_train_info в текущее время
        train_info.datetime_end_train_info = datetime.now()
        
        # Сохраняем изменения
        await session.commit()
        
        return StatusResponse(
            status=True,
            message="Тренировка успешно завершена"
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при завершении тренировки: {str(e)}"
        )