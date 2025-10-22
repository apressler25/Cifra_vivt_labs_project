




























#создание тестовых данных в бд

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from db.engine import get_async_session

from datetime import datetime, timedelta
from models.models_bd import (
    Base, TargetMuscleCategory, User, WorkoutExercises, ProgramsWorkout, 
    WorkoutExPool, TrainInfo, TrainPool, ApproachesRec, Restrictions
)

async def create_test_data(session:AsyncSession):
    """Создание тестовых данных для всех таблиц"""
    
    # 1. Target_muscle_category
    muscle_categories = [
        TargetMuscleCategory(id_muscle_category=1, name_muscle_category="Грудь"),
        TargetMuscleCategory(id_muscle_category=2, name_muscle_category="Спина"),
        TargetMuscleCategory(id_muscle_category=3, name_muscle_category="Ноги")
    ]
    session.add_all(muscle_categories)
    await session.flush()
    
    # 2. User
    users = [
        User(
            id_user=1001,
            id_telegram=111111111,
            name_user="Иван Петров",
            info_restrictions_user="Проблемы с коленом",
            sub_user=True
        ),
        User(
            id_user=1002, 
            id_telegram=222222222,
            name_user="Мария Сидорова",
            info_restrictions_user="Астма",
            sub_user=False
        ),
        User(
            id_user=1003,
            id_telegram=333333333, 
            name_user="Алексей Козлов",
            info_restrictions_user=None,
            sub_user=True
        )
    ]
    session.add_all(users)
    await session.flush()
    
    # 3. Workout_exercises
    workout_exercises = [
        WorkoutExercises(
            id_workout_exercises=2001,
            name_workout_exercises="Жим штанги лежа",
            id_creation_user="trainer1",
            notice_workout_exercises="Базовое упражнение для груди",
            id_muscle_category=1,
            gif_file_workout_exercises=None
        ),
        WorkoutExercises(
            id_workout_exercises=2002,
            name_workout_exercises="Тяга верхнего блока",
            id_creation_user="trainer1", 
            notice_workout_exercises="Для развития широчайших мышц",
            id_muscle_category=2,
            gif_file_workout_exercises=None
        ),
        WorkoutExercises(
            id_workout_exercises=2003,
            name_workout_exercises="Приседания со штангой",
            id_creation_user="trainer2",
            notice_workout_exercises="Основное упражнение для ног",
            id_muscle_category=3,
            gif_file_workout_exercises=None
        )
    ]
    session.add_all(workout_exercises)
    await session.flush()
    
    # 4. Programs_workout
    programs_workout = [
        ProgramsWorkout(
            id_programs_workout=3001,
            name_programs_workout="Силовая тренировка груди",
            id_user=1001,
            week_day_programs_workout="Понедельник"
        ),
        ProgramsWorkout(
            id_programs_workout=3002,
            name_programs_workout="Тренировка спины",
            id_user=1002, 
            week_day_programs_workout="Среда"
        ),
        ProgramsWorkout(
            id_programs_workout=3003,
            name_programs_workout="Ножной день",
            id_user=1003,
            week_day_programs_workout="Пятница"
        )
    ]
    session.add_all(programs_workout)
    await session.flush()
    
    # 5. Workout_ex_pool
    workout_ex_pool = [
        WorkoutExPool(
            id_ex_pool=4001,
            id_programs_workout=3001,
            id_workout_exercises=2001,
            max_target_iteration_ex_pool=12,
            min_target_iteration_ex_pool=8,
            approaches_target_ex_pool=4,
            weight_ex_pool=50
        ),
        WorkoutExPool(
            id_ex_pool=4002,
            id_programs_workout=3002,
            id_workout_exercises=2002,
            max_target_iteration_ex_pool=15,
            min_target_iteration_ex_pool=10,
            approaches_target_ex_pool=3,
            weight_ex_pool=40
        ),
        WorkoutExPool(
            id_ex_pool=4003,
            id_programs_workout=3003,
            id_workout_exercises=2003,
            max_target_iteration_ex_pool=10,
            min_target_iteration_ex_pool=6,
            approaches_target_ex_pool=5,
            weight_ex_pool=60
        )
    ]
    session.add_all(workout_ex_pool)
    await session.flush()
    
    # 6. Train_info
    train_info = [
        TrainInfo(
            id_train_info=5001,
            datetime_start_train_info=datetime.now() - timedelta(days=2),
            datetime_end_train_info=datetime.now() - timedelta(days=2, hours=1),
            check_train_info=True  # завершенная
        ),
        TrainInfo(
            id_train_info=5002,
            datetime_start_train_info=datetime.now() - timedelta(days=1),
            datetime_end_train_info=datetime.now() - timedelta(days=1, hours=1),
            check_train_info=True  # завершенная
        ),
        TrainInfo(
            id_train_info=5003,
            datetime_start_train_info=datetime.now(),
            datetime_end_train_info=None,
            check_train_info=False  # активная тренировка
        )
    ]
    session.add_all(train_info)
    await session.flush()
    
    # 7. Train_pool
    train_pool = [
        TrainPool(
            id_train_pool=6001,
            id_train_info=5001,
            id_ex_pool=4001,
            record_bool=False
        ),
        TrainPool(
            id_train_pool=6002,
            id_train_info=5002,
            id_ex_pool=4002,
            record_bool=True
        ),
        TrainPool(
            id_train_pool=6003,
            id_train_info=5003,
            id_ex_pool=4003,
            record_bool=False
        )
    ]
    session.add_all(train_pool)
    await session.flush()
    
    # 8. Approaches_rec
    approaches_rec = [
        ApproachesRec(
            id_approaches_rec=7001,
            weight_approaches_rec=50,
            rest_time_up_approaches_rec=datetime.now() - timedelta(minutes=5),
            rest_time_num_approaches_rec=120,
            num_iteration_approaches_rec=10,
            id_train_pool=6001
        ),
        ApproachesRec(
            id_approaches_rec=7002,
            weight_approaches_rec=40,
            rest_time_up_approaches_rec=datetime.now() - timedelta(minutes=3),
            rest_time_num_approaches_rec=90,
            num_iteration_approaches_rec=12,
            id_train_pool=6002
        ),
        ApproachesRec(
            id_approaches_rec=7003,
            weight_approaches_rec=60,
            rest_time_up_approaches_rec=None,
            rest_time_num_approaches_rec=180,
            num_iteration_approaches_rec=8,
            id_train_pool=6003
        )
    ]
    session.add_all(approaches_rec)
    await session.flush()
    
    # 9. Restrictions
    restrictions = [
        Restrictions(
            id_restrictions=8001,
            id_workout_exercises=2001,
            id_user=1001
        ),
        Restrictions(
            id_restrictions=8002,
            id_workout_exercises=2002,
            id_user=1002
        ),
        Restrictions(
            id_restrictions=8003,
            id_workout_exercises=2003,
            id_user=1003
        )
    ]
    session.add_all(restrictions)
    
    # Фиксируем все изменения
    await session.commit()
    return("✅ Тестовые данные успешно добавлены во все таблицы!")
