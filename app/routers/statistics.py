
from fastapi import APIRouter, Depends, HTTPException, Response
from schemas.statistics_schema import UserRecord, UserRecordsResponse, WeeklyMuscleGroupsResponse, LastWorkoutsStatsResponse, ExerciseStats, ExercisePoint
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select
from sqlalchemy import delete 
from pydantic import TypeAdapter
from models.models_bd import (User, TrainInfo, TrainPool, WorkoutExPool, ProgramsWorkout, 
                            WorkoutExercises,TargetMuscleCategory,ApproachesRec, Restrictions)
from sqlalchemy.orm import selectinload
from fastapi.responses import RedirectResponse
from sqlalchemy import func, extract, and_, or_
from datetime import datetime, date, timedelta
from schemas.user_schemas import StatusResponse


statistics_router = APIRouter(prefix="/statistics", tags=["СТАТИСТИКА"])


    
@statistics_router.get("/records/{user_id}", 
                        summary="Получение рекордов пользователя",
                        response_model=UserRecordsResponse)
async def get_user_records(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        records = []
        
        # 1. Максимальный вес по упражнениям
        max_weight_stmt = (
            select(
                WorkoutExercises.name_workout_exercises,
                func.max(ApproachesRec.weight_approaches_rec).label('max_weight'),
                func.max(TrainInfo.datetime_start_train_info).label('latest_date')
            )
            .select_from(ApproachesRec)
            .join(TrainPool, TrainPool.id_train_pool == ApproachesRec.id_train_pool)
            .join(TrainInfo, TrainInfo.id_train_info == TrainPool.id_train_info)
            .join(WorkoutExercises, WorkoutExercises.id_workout_exercises == TrainPool.id_workout_exercises)
            .where(
                and_(
                    TrainInfo.Id_user == user_id,
                    ApproachesRec.weight_approaches_rec > 0,
                    TrainInfo.check_train_info == True,
                    TrainInfo.datetime_end_train_info.isnot(None)
                )
            )
            .group_by(WorkoutExercises.name_workout_exercises)
            .order_by(func.max(ApproachesRec.weight_approaches_rec).desc())
            .limit(3)
        )
        
        result = await session.execute(max_weight_stmt)
        max_weight_records = result.all()
        
        for exercise_name, max_weight, latest_date in max_weight_records:
            if max_weight and latest_date:
                records.append(UserRecord(
                    main_text=f"Максимум в {exercise_name}: {max_weight} кг",
                    description_text=f"Установлен {latest_date.strftime('%Y-%m-%d')}"
                ))
        
        
        # 2. Самая длительная тренировка
        duration_stmt = (
            select(
                TrainInfo.datetime_start_train_info,
                TrainInfo.datetime_end_train_info,
                (func.extract('epoch', TrainInfo.datetime_end_train_info - TrainInfo.datetime_start_train_info) / 60).label('duration_minutes')
            )
            .where(
                and_(
                    TrainInfo.Id_user == user_id,
                    TrainInfo.check_train_info == True,
                    TrainInfo.datetime_end_train_info.isnot(None),
                    TrainInfo.datetime_start_train_info.isnot(None)
                )
            )
            .order_by((func.extract('epoch', TrainInfo.datetime_end_train_info - TrainInfo.datetime_start_train_info) / 60).desc())
            .limit(1)
        )
        
        result = await session.execute(duration_stmt)
        longest_workout = result.first()
        
        if longest_workout and longest_workout.duration_minutes:
            duration_minutes = int(longest_workout.duration_minutes)
            records.append(UserRecord(
                main_text=f"Рекорд длительности: {duration_minutes} минут",
                description_text=f"Тренировка {longest_workout.datetime_start_train_info.strftime('%Y-%m-%d')}"
            ))
        
        # 3. Последняя завершенная тренировка
        last_workout_stmt = (
            select(
                TrainInfo.datetime_start_train_info,
                TrainInfo.name_programs_workout
            )
            .where(
                and_(
                    TrainInfo.Id_user == user_id,
                    TrainInfo.check_train_info == True,
                    TrainInfo.datetime_end_train_info.isnot(None)
                )
            )
            .order_by(TrainInfo.datetime_start_train_info.desc())
            .limit(1)
        )
        
        result = await session.execute(last_workout_stmt)
        last_workout = result.first()
        
        if last_workout:
            records.append(UserRecord(
                main_text=f"Последняя тренировка: {last_workout.name_programs_workout}",
                description_text=f"Завершена {last_workout.datetime_start_train_info.strftime('%Y-%m-%d')}"
            ))
        
        return UserRecordsResponse(data=records)
        
    except Exception as e:
        return UserRecordsResponse(data=[])
        # UserRecordsResponse UserRecord
        
        
@statistics_router.get("/weeklymuscles/{user_id}", 
                        summary="Получение списка задействованных групп мышц за неделю",
                        response_model=WeeklyMuscleGroupsResponse)
async def get_user_records(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        week_ago = datetime.now() - timedelta(days=7)
        
        # Запрос только для завершенных тренировок
        stmt = (
            select(WorkoutExercises.id_muscle_category)
            .select_from(TrainInfo)
            .join(TrainPool, TrainInfo.id_train_info == TrainPool.id_train_info)
            .join(WorkoutExercises, TrainPool.id_workout_exercises == WorkoutExercises.id_workout_exercises)
            .where(
                and_(
                    TrainInfo.Id_user == user_id,
                    TrainInfo.datetime_start_train_info >= week_ago,
                    TrainInfo.check_train_info == True,  # Только завершенные
                    TrainInfo.datetime_start_train_info <= datetime.now()  # Не будущие даты
                )
            )
            .distinct()
            .order_by(WorkoutExercises.id_muscle_category)
        )
        
        result = await session.execute(stmt)
        muscle_group_ids = result.scalars().all()
        
        return WeeklyMuscleGroupsResponse(muscle_ids=muscle_group_ids)
        
    except Exception as e:
        return WeeklyMuscleGroupsResponse(muscle_ids=[])
    
    
    
    
@statistics_router.get("/lastworkouts/{user_id}", 
                        summary="Получение статистики за последние 5 тренировок",
                        response_model=LastWorkoutsStatsResponse)
async def get_user_records(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        # Получаем последние 5 тренировок
        last_workouts_stmt = (
            select(TrainInfo.id_train_info, TrainInfo.datetime_start_train_info)
            .where(
                and_(
                    TrainInfo.Id_user == user_id,
                    TrainInfo.check_train_info == True
                )
            )
            .order_by(TrainInfo.datetime_start_train_info.desc())
            .limit(5)
        )
        
        result = await session.execute(last_workouts_stmt)
        last_workouts = result.all()
        
        if not last_workouts:
            return LastWorkoutsStatsResponse(last_workout_stats=[])
        
        workout_ids = [workout.id_train_info for workout in last_workouts]
        workout_dates = {workout.id_train_info: workout.datetime_start_train_info for workout in last_workouts}
        
        # Получаем подходы с сортировкой по дате
        approaches_stmt = (
            select(
                TrainPool.id_train_info,
                WorkoutExercises.name_workout_exercises,
                ApproachesRec.weight_approaches_rec,
                ApproachesRec.num_iteration_approaches_rec
            )
            .select_from(ApproachesRec)
            .join(TrainPool, TrainPool.id_train_pool == ApproachesRec.id_train_pool)
            .join(WorkoutExercises, WorkoutExercises.id_workout_exercises == TrainPool.id_workout_exercises)
            .where(TrainPool.id_train_info.in_(workout_ids))
            .order_by(TrainPool.id_train_info.desc(), WorkoutExercises.name_workout_exercises)
        )
        
        result = await session.execute(approaches_stmt)
        approaches_data = result.all()
        
        # Группируем и сортируем по дате (от новых к старым)
        exercise_stats_dict = {}
        
        for workout_id, exercise_name, weight, repetitions in approaches_data:
            if exercise_name not in exercise_stats_dict:
                exercise_stats_dict[exercise_name] = ExerciseStats(
                    exercise_name=exercise_name,
                    sets=[]
                )
            
            workout_date = workout_dates[workout_id]
            date_str = workout_date.strftime("%Y-%m-%d")
            
            exercise_stats_dict[exercise_name].sets.append(
                ExercisePoint(
                    weight=float(weight),
                    num_iteration=repetitions,
                    daate=date_str
                )
            )
        
        # Сортируем подходы внутри каждого упражнения по дате (от новых к старым)
        for exercise in exercise_stats_dict.values():
            exercise.sets.sort(key=lambda x: x.daate, reverse=True)
        
        last_workout_stats = list(exercise_stats_dict.values())
        
        return LastWorkoutsStatsResponse(last_workout_stats=last_workout_stats)
        
    except Exception as e:
        return LastWorkoutsStatsResponse(last_workout_stats=[])