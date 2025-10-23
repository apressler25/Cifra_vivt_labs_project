
#создание тестовых данных в бд

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from db.engine import get_async_session

from datetime import datetime, timedelta
from models.models_bd import (
    Base, TargetMuscleCategory, User, WorkoutExercises, ProgramsWorkout, 
    WorkoutExPool, TrainInfo, TrainPool, ApproachesRec, Restrictions
)
# async def create_test_data(session: AsyncSession):
#     """Создание тестовых данных для всех таблиц"""
    
#     # 1. Target_muscle_category
#     muscle_categories = [
#         TargetMuscleCategory(id_muscle_category=1, name_muscle_category="Грудь"),
#         TargetMuscleCategory(id_muscle_category=2, name_muscle_category="Спина"),
#         TargetMuscleCategory(id_muscle_category=3, name_muscle_category="Ноги"),
#         TargetMuscleCategory(id_muscle_category=4, name_muscle_category="Плечи"),
#         TargetMuscleCategory(id_muscle_category=5, name_muscle_category="Руки")
#     ]
#     session.add_all(muscle_categories)
#     await session.flush()
    
#     # 2. User
#     users = [
#         User(
#             id_telegram=1001,
#             name_user="Иван Петров",
#             info_restrictions_user="Проблемы с коленом",
#             sub_user=True
#         ),
#         User(
#             id_telegram=1002,
#             name_user="Мария Сидорова", 
#             info_restrictions_user="Астма",
#             sub_user=False
#         ),
#         User(
#             id_telegram=1003,
#             name_user="Алексей Козлов",
#             info_restrictions_user=None,
#             sub_user=True
#         ),
#         User(
#             id_telegram=1004,
#             name_user="Екатерина Новикова",
#             info_restrictions_user="Боль в спине",
#             sub_user=True
#         ),
#         User(
#             id_telegram=1005,
#             name_user="Дмитрий Волков",
#             info_restrictions_user=None,
#             sub_user=False
#         )
#     ]
#     session.add_all(users)
#     await session.flush()
    
#     # 3. Workout_exercises
#     workout_exercises = [
#         WorkoutExercises(
#             id_workout_exercises=2001,
#             name_workout_exercises="Жим штанги лежа",
#             id_creation_user=1001,
#             notice_workout_exercises="Базовое упражнение для груди",
#             id_muscle_category=1,
#             gif_file_workout_exercises=None,
#             vision_user=True
#         ),
#         WorkoutExercises(
#             id_workout_exercises=2002,
#             name_workout_exercises="Тяга верхнего блока",
#             id_creation_user=1001,
#             notice_workout_exercises="Для развития широчайших мышц",
#             id_muscle_category=2,
#             gif_file_workout_exercises=None,
#             vision_user=True
#         ),
#         WorkoutExercises(
#             id_workout_exercises=2003,
#             name_workout_exercises="Приседания со штангой",
#             id_creation_user=1002,
#             notice_workout_exercises="Основное упражнение для ног",
#             id_muscle_category=3,
#             gif_file_workout_exercises=None,
#             vision_user=True
#         ),
#         WorkoutExercises(
#             id_workout_exercises=2004,
#             name_workout_exercises="Жим гантелей сидя",
#             id_creation_user=1003,
#             notice_workout_exercises="Для развития плеч",
#             id_muscle_category=4,
#             gif_file_workout_exercises=None,
#             vision_user=True
#         ),
#         WorkoutExercises(
#             id_workout_exercises=2005,
#             name_workout_exercises="Подъем штанги на бицепс",
#             id_creation_user=1004,
#             notice_workout_exercises="Изолирующее упражнение для бицепса",
#             id_muscle_category=5,
#             gif_file_workout_exercises=None,
#             vision_user=True
#         )
#     ]
#     session.add_all(workout_exercises)
#     await session.flush()
    
#     # 4. Programs_workout
#     programs_workout = [
#         ProgramsWorkout(
#             id_programs_workout=3001,
#             name_programs_workout="Силовая тренировка груди",
#             id_user=1001,
#             week_day_programs_workout="Понедельник"
#         ),
#         ProgramsWorkout(
#             id_programs_workout=3002,
#             name_programs_workout="Тренировка спины",
#             id_user=1002,
#             week_day_programs_workout="Среда"
#         ),
#         ProgramsWorkout(
#             id_programs_workout=3003,
#             name_programs_workout="Ножной день",
#             id_user=1003,
#             week_day_programs_workout="Пятница"
#         ),
#         ProgramsWorkout(
#             id_programs_workout=3004,
#             name_programs_workout="Тренировка плеч",
#             id_user=1004,
#             week_day_programs_workout="Вторник"
#         ),
#         ProgramsWorkout(
#             id_programs_workout=3005,
#             name_programs_workout="Тренировка рук",
#             id_user=1005,
#             week_day_programs_workout="Четверг"
#         )
#     ]
#     session.add_all(programs_workout)
#     await session.flush()
    
#     # 5. Workout_ex_pool
#     workout_ex_pool = [
#         WorkoutExPool(
#             id_ex_pool=4001,
#             id_programs_workout=3001,
#             id_workout_exercises=2001,
#             max_target_iteration_ex_pool=12,
#             min_target_iteration_ex_pool=8,
#             approaches_target_ex_pool=4,
#             weight_ex_pool=50
#         ),
#         WorkoutExPool(
#             id_ex_pool=4002,
#             id_programs_workout=3002,
#             id_workout_exercises=2002,
#             max_target_iteration_ex_pool=15,
#             min_target_iteration_ex_pool=10,
#             approaches_target_ex_pool=3,
#             weight_ex_pool=40
#         ),
#         WorkoutExPool(
#             id_ex_pool=4003,
#             id_programs_workout=3003,
#             id_workout_exercises=2003,
#             max_target_iteration_ex_pool=10,
#             min_target_iteration_ex_pool=6,
#             approaches_target_ex_pool=5,
#             weight_ex_pool=60
#         ),
#         WorkoutExPool(
#             id_ex_pool=4004,
#             id_programs_workout=3004,
#             id_workout_exercises=2004,
#             max_target_iteration_ex_pool=12,
#             min_target_iteration_ex_pool=10,
#             approaches_target_ex_pool=4,
#             weight_ex_pool=25
#         ),
#         WorkoutExPool(
#             id_ex_pool=4005,
#             id_programs_workout=3005,
#             id_workout_exercises=2005,
#             max_target_iteration_ex_pool=15,
#             min_target_iteration_ex_pool=12,
#             approaches_target_ex_pool=3,
#             weight_ex_pool=30
#         )
#     ]
#     session.add_all(workout_ex_pool)
#     await session.flush()
    
#     # 6. Train_info
#     train_info = [
#         TrainInfo(
#             id_train_info=5001,
#             datetime_start_train_info=datetime.now() - timedelta(days=2),
#             datetime_end_train_info=datetime.now() - timedelta(days=2, hours=1),
#             check_train_info=True,
#             Id_user=1001,
#             name_programs_workout="Силовая тренировка груди"
#         ),
#         TrainInfo(
#             id_train_info=5002,
#             datetime_start_train_info=datetime.now() - timedelta(days=1),
#             datetime_end_train_info=datetime.now() - timedelta(days=1, hours=1),
#             check_train_info=True,
#             Id_user=1002,
#             name_programs_workout="Тренировка спины"
#         ),
#         TrainInfo(
#             id_train_info=5003,
#             datetime_start_train_info=datetime.now(),
#             datetime_end_train_info=None,
#             check_train_info=False,
#             Id_user=1003,
#             name_programs_workout="Ножной день"
#         ),
#         TrainInfo(
#             id_train_info=5004,
#             datetime_start_train_info=datetime.now() - timedelta(days=3),
#             datetime_end_train_info=datetime.now() - timedelta(days=3, hours=1),
#             check_train_info=True,
#             Id_user=1004,
#             name_programs_workout="Тренировка плеч"
#         ),
#         TrainInfo(
#             id_train_info=5005,
#             datetime_start_train_info=datetime.now() - timedelta(days=4),
#             datetime_end_train_info=datetime.now() - timedelta(days=4, hours=1),
#             check_train_info=True,
#             Id_user=1005,
#             name_programs_workout="Тренировка рук"
#         )
#     ]
#     session.add_all(train_info)
#     await session.flush()
    
#     # 7. Train_pool
#     train_pool = [
#         TrainPool(
#             id_train_pool=6001,
#             id_train_info=5001,
#             record_bool=False,
#             id_workout_exercises=2001
#         ),
#         TrainPool(
#             id_train_pool=6002,
#             id_train_info=5002,
#             record_bool=True,
#             id_workout_exercises=2002
#         ),
#         TrainPool(
#             id_train_pool=6003,
#             id_train_info=5003,
#             record_bool=False,
#             id_workout_exercises=2003
#         ),
#         TrainPool(
#             id_train_pool=6004,
#             id_train_info=5004,
#             record_bool=True,
#             id_workout_exercises=2004
#         ),
#         TrainPool(
#             id_train_pool=6005,
#             id_train_info=5005,
#             record_bool=False,
#             id_workout_exercises=2005
#         )
#     ]
#     session.add_all(train_pool)
#     await session.flush()
    
#     # 8. Approaches_rec
#     approaches_rec = [
#         ApproachesRec(
#             id_approaches_rec=7001,
#             weight_approaches_rec=50,
#             rest_time_up_approaches_rec=datetime.now() - timedelta(minutes=5),
#             rest_time_down_approaches_rec=datetime.now() - timedelta(minutes=4),
#             num_iteration_approaches_rec=10,
#             id_train_pool=6001
#         ),
#         ApproachesRec(
#             id_approaches_rec=7002,
#             weight_approaches_rec=40,
#             rest_time_up_approaches_rec=datetime.now() - timedelta(minutes=3),
#             rest_time_down_approaches_rec=datetime.now() - timedelta(minutes=2),
#             num_iteration_approaches_rec=12,
#             id_train_pool=6002
#         ),
#         ApproachesRec(
#             id_approaches_rec=7003,
#             weight_approaches_rec=60,
#             rest_time_up_approaches_rec=None,
#             rest_time_down_approaches_rec=None,
#             num_iteration_approaches_rec=8,
#             id_train_pool=6003
#         ),
#         ApproachesRec(
#             id_approaches_rec=7004,
#             weight_approaches_rec=25,
#             rest_time_up_approaches_rec=datetime.now() - timedelta(minutes=4),
#             rest_time_down_approaches_rec=datetime.now() - timedelta(minutes=3),
#             num_iteration_approaches_rec=11,
#             id_train_pool=6004
#         ),
#         ApproachesRec(
#             id_approaches_rec=7005,
#             weight_approaches_rec=30,
#             rest_time_up_approaches_rec=datetime.now() - timedelta(minutes=6),
#             rest_time_down_approaches_rec=datetime.now() - timedelta(minutes=5),
#             num_iteration_approaches_rec=13,
#             id_train_pool=6005
#         )
#     ]
#     session.add_all(approaches_rec)
#     await session.flush()
    
#     # 9. Restrictions
#     restrictions = [
#         Restrictions(
#             id_restrictions=8001,
#             id_workout_exercises=2001,
#             id_user=1001
#         ),
#         Restrictions(
#             id_restrictions=8002,
#             id_workout_exercises=2002,
#             id_user=1002
#         ),
#         Restrictions(
#             id_restrictions=8003,
#             id_workout_exercises=2003,
#             id_user=1003
#         ),
#         Restrictions(
#             id_restrictions=8004,
#             id_workout_exercises=2004,
#             id_user=1004
#         ),
#         Restrictions(
#             id_restrictions=8005,
#             id_workout_exercises=2005,
#             id_user=1005
#         )
#     ]
#     session.add_all(restrictions)
    
#     # Фиксируем все изменения
#     await session.commit()
#     return "✅ Тестовые данные успешно добавлены во все таблицы!"

async def create_test_data(session: AsyncSession):
    """Создание тестовых данных для всех таблиц"""
    
    # 1. Target_muscle_category
    muscle_categories = [
        TargetMuscleCategory(id_muscle_category=1, name_muscle_category="Грудь"),
        TargetMuscleCategory(id_muscle_category=2, name_muscle_category="Спина"),
        TargetMuscleCategory(id_muscle_category=3, name_muscle_category="Ноги"),
        TargetMuscleCategory(id_muscle_category=4, name_muscle_category="Плечи"),
        TargetMuscleCategory(id_muscle_category=5, name_muscle_category="Руки")
    ]
    session.add_all(muscle_categories)
    await session.flush()
    
    # 2. User (3 пользователя)
    users = [
        User(
            id_telegram=1001,
            name_user="Иван Петров",
            info_restrictions_user="Проблемы с коленом",
            sub_user=True
        ),
        User(
            id_telegram=1002,
            name_user="Мария Сидорова", 
            info_restrictions_user="Астма",
            sub_user=False
        ),
        User(
            id_telegram=1003,
            name_user="Алексей Козлов",
            info_restrictions_user=None,
            sub_user=True
        )
    ]
    session.add_all(users)
    await session.flush()
    
    # 3. Workout_exercises (больше упражнений для разнообразия)
    workout_exercises = [
        # Упражнения для груди
        WorkoutExercises(id_workout_exercises=2001, name_workout_exercises="Жим штанги лежа", id_creation_user=1001, notice_workout_exercises="Базовое упражнение для груди", id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
        WorkoutExercises(id_workout_exercises=2002, name_workout_exercises="Жим гантелей лежа", id_creation_user=1001, notice_workout_exercises="Для развития грудных мышц", id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
        WorkoutExercises(id_workout_exercises=2003, name_workout_exercises="Разводка гантелей", id_creation_user=1001, notice_workout_exercises="Изолирующее упражнение", id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для спины
        WorkoutExercises(id_workout_exercises=2004, name_workout_exercises="Тяга верхнего блока", id_creation_user=1002, notice_workout_exercises="Для развития широчайших мышц", id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
        WorkoutExercises(id_workout_exercises=2005, name_workout_exercises="Тяга штанги в наклоне", id_creation_user=1002, notice_workout_exercises="Базовое упражнение для спины", id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
        WorkoutExercises(id_workout_exercises=2006, name_workout_exercises="Тяга гантели одной рукой", id_creation_user=1002, notice_workout_exercises="Для глубины мышц спины", id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для ног
        WorkoutExercises(id_workout_exercises=2007, name_workout_exercises="Приседания со штангой", id_creation_user=1003, notice_workout_exercises="Основное упражнение для ног", id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        WorkoutExercises(id_workout_exercises=2008, name_workout_exercises="Жим ногами", id_creation_user=1003, notice_workout_exercises="Для квадрицепсов", id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        WorkoutExercises(id_workout_exercises=2009, name_workout_exercises="Выпады с гантелями", id_creation_user=1003, notice_workout_exercises="Для ягодичных мышц", id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для плеч
        WorkoutExercises(id_workout_exercises=2010, name_workout_exercises="Жим гантелей сидя", id_creation_user=1001, notice_workout_exercises="Для развития плеч", id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        WorkoutExercises(id_workout_exercises=2011, name_workout_exercises="Махи гантелями в стороны", id_creation_user=1002, notice_workout_exercises="Для средних пучков дельт", id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для рук
        WorkoutExercises(id_workout_exercises=2012, name_workout_exercises="Подъем штанги на бицепс", id_creation_user=1003, notice_workout_exercises="Изолирующее упражнение для бицепса", id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
        WorkoutExercises(id_workout_exercises=2013, name_workout_exercises="Французский жим", id_creation_user=1001, notice_workout_exercises="Для трицепса", id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
    ]
    session.add_all(workout_exercises)
    await session.flush()
    
    # 4. Programs_workout (по 2-3 программы на пользователя)
    programs_workout = [
        # Программы для пользователя 1001
        ProgramsWorkout(id_programs_workout=3001, name_programs_workout="Силовая тренировка груди", id_user=1001, week_day_programs_workout="Понедельник"),
        ProgramsWorkout(id_programs_workout=3002, name_programs_workout="Тренировка спины", id_user=1001, week_day_programs_workout="Среда"),
        ProgramsWorkout(id_programs_workout=3003, name_programs_workout="Тренировка ног", id_user=1001, week_day_programs_workout="Пятница"),
        
        # Программы для пользователя 1002
        ProgramsWorkout(id_programs_workout=3004, name_programs_workout="Верх тела", id_user=1002, week_day_programs_workout="Понедельник"),
        ProgramsWorkout(id_programs_workout=3005, name_programs_workout="Низ тела", id_user=1002, week_day_programs_workout="Среда"),
        ProgramsWorkout(id_programs_workout=3006, name_programs_workout="Кардио", id_user=1002, week_day_programs_workout="Пятница"),
        
        # Программы для пользователя 1003
        ProgramsWorkout(id_programs_workout=3007, name_programs_workout="Фуллбади", id_user=1003, week_day_programs_workout="Понедельник"),
        ProgramsWorkout(id_programs_workout=3008, name_programs_workout="Спина-бицепс", id_user=1003, week_day_programs_workout="Среда"),
    ]
    session.add_all(programs_workout)
    await session.flush()
    
    # 5. Workout_ex_pool (по 3 упражнения на программу)
    workout_ex_pool = []
    ex_pool_id = 4001
    
    # Программа 3001 (Грудь) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3001, id_workout_exercises=2001, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=50),
        WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3001, id_workout_exercises=2002, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=20),
        WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3001, id_workout_exercises=2003, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=4, weight_ex_pool=15),
    ])
    ex_pool_id += 3
    
    # Программа 3002 (Спина) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3002, id_workout_exercises=2004, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=40),
        WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3002, id_workout_exercises=2005, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=6, approaches_target_ex_pool=3, weight_ex_pool=60),
        WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3002, id_workout_exercises=2006, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=4, weight_ex_pool=25),
    ])
    ex_pool_id += 3
    
    # Программа 3003 (Ноги) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3003, id_workout_exercises=2007, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=6, approaches_target_ex_pool=5, weight_ex_pool=80),
        WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3003, id_workout_exercises=2008, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=100),
        WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3003, id_workout_exercises=2009, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=15),
    ])
    ex_pool_id += 3
    
    # Программа 3004 (Верх тела) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3004, id_workout_exercises=2001, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=45),
        WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3004, id_workout_exercises=2004, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=35),
        WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3004, id_workout_exercises=2010, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=18),
    ])
    ex_pool_id += 3
    
    # Программа 3005 (Низ тела) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3005, id_workout_exercises=2007, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=5, weight_ex_pool=70),
        WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3005, id_workout_exercises=2008, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=90),
        WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3005, id_workout_exercises=2009, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=12),
    ])
    ex_pool_id += 3
    
    # Программа 3006 (Кардио) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3006, id_workout_exercises=2007, max_target_iteration_ex_pool=20, min_target_iteration_ex_pool=15, approaches_target_ex_pool=3, weight_ex_pool=50),
        WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3006, id_workout_exercises=2009, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=10),
        WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3006, id_workout_exercises=2011, max_target_iteration_ex_pool=20, min_target_iteration_ex_pool=15, approaches_target_ex_pool=3, weight_ex_pool=8),
    ])
    ex_pool_id += 3
    
    # Программа 3007 (Фуллбади) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3007, id_workout_exercises=2001, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=6, approaches_target_ex_pool=4, weight_ex_pool=55),
        WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3007, id_workout_exercises=2005, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=3, weight_ex_pool=65),
        WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3007, id_workout_exercises=2007, max_target_iteration_ex_pool=8, min_target_iteration_ex_pool=5, approaches_target_ex_pool=5, weight_ex_pool=85),
    ])
    ex_pool_id += 3
    
    # Программа 3008 (Спина-бицепс) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3008, id_workout_exercises=2004, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=4, weight_ex_pool=38),
        WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3008, id_workout_exercises=2006, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=3, weight_ex_pool=22),
        WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3008, id_workout_exercises=2012, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=30),
    ])
    
    session.add_all(workout_ex_pool)
    await session.flush()
    
    # 6. Train_info (по 3-5 тренировок на пользователя)
    train_info = []
    train_info_id = 5001
    
    # Тренировки для пользователя 1001 (5 тренировок)
    for i in range(5):
        train_info.append(TrainInfo(
            id_train_info=train_info_id,
            datetime_start_train_info=datetime.now() - timedelta(days=7-i),
            datetime_end_train_info=datetime.now() - timedelta(days=7-i, hours=1, minutes=30),
            check_train_info=True,
            Id_user=1001,
            name_programs_workout=["Силовая тренировка груди", "Тренировка спины", "Тренировка ног"][i % 3]
        ))
        train_info_id += 1
    
    # Тренировки для пользователя 1002 (4 тренировки)
    for i in range(4):
        train_info.append(TrainInfo(
            id_train_info=train_info_id,
            datetime_start_train_info=datetime.now() - timedelta(days=5-i),
            datetime_end_train_info=datetime.now() - timedelta(days=5-i, hours=1, minutes=15),
            check_train_info=True,
            Id_user=1002,
            name_programs_workout=["Верх тела", "Низ тела", "Кардио"][i % 3]
        ))
        train_info_id += 1
    
    # Тренировки для пользователя 1003 (3 тренировки)
    for i in range(3):
        train_info.append(TrainInfo(
            id_train_info=train_info_id,
            datetime_start_train_info=datetime.now() - timedelta(days=3-i),
            datetime_end_train_info=datetime.now() - timedelta(days=3-i, hours=1, minutes=45),
            check_train_info=True,
            Id_user=1003,
            name_programs_workout=["Фуллбади", "Спина-бицепс"][i % 2]
        ))
        train_info_id += 1
    
    session.add_all(train_info)
    await session.flush()
    
    # 7. Train_pool (по 3-4 упражнения на тренировку)
    train_pool = []
    train_pool_id = 6001
    
    # Для каждой тренировки создаем по 3-4 упражнения
    for train in train_info:
        num_exercises = 3 if train.id_train_info % 2 == 0 else 4
        
        # Выбираем случайные упражнения из соответствующих программ
        program_exercises = [ex for ex in workout_ex_pool if ex.id_programs_workout in [
            pw.id_programs_workout for pw in programs_workout 
            if pw.name_programs_workout == train.name_programs_workout
        ]]
        
        selected_exercises = program_exercises[:num_exercises]
        
        for ex in selected_exercises:
            train_pool.append(TrainPool(
                id_train_pool=train_pool_id,
                id_train_info=train.id_train_info,
                record_bool=(train_pool_id % 3 == 0),  # Каждая третья запись - рекорд
                id_workout_exercises=ex.id_workout_exercises
            ))
            train_pool_id += 1
    
    session.add_all(train_pool)
    await session.flush()
    
    # 8. Approaches_rec (по 3-4 подхода на упражнение)
    approaches_rec = []
    approach_id = 7001
    
    for train_pool_item in train_pool:
        num_approaches = 3 if approach_id % 2 == 0 else 4
        
        for approach_num in range(num_approaches):
            weight = train_pool_item.id_workout_exercises * 2 + approach_num * 5  # Простая логика веса
            iterations = 8 + approach_num * 2  # Простая логика повторений
            
            approaches_rec.append(ApproachesRec(
                id_approaches_rec=approach_id,
                weight_approaches_rec=weight,
                rest_time_up_approaches_rec=datetime.now() - timedelta(minutes=(10 + approach_num)),
                rest_time_down_approaches_rec=datetime.now() - timedelta(minutes=(9 + approach_num)),
                num_iteration_approaches_rec=iterations,
                id_train_pool=train_pool_item.id_train_pool
            ))
            approach_id += 1
    
    session.add_all(approaches_rec)
    await session.flush()
    
    # 9. Restrictions (по 1-2 ограничения на пользователя)
    restrictions = [
        Restrictions(id_restrictions=8001, id_workout_exercises=2007, id_user=1001),  # Иван - проблемы с приседаниями
        Restrictions(id_restrictions=8002, id_workout_exercises=2001, id_user=1002),  # Мария - проблемы с жимом
        Restrictions(id_restrictions=8003, id_workout_exercises=2004, id_user=1002),  # Мария - проблемы с тягой
        Restrictions(id_restrictions=8004, id_workout_exercises=2008, id_user=1003),  # Алексей - проблемы с жимом ногами
    ]
    session.add_all(restrictions)
    
    # Фиксируем все изменения
    await session.commit()
    return "✅ Тестовые данные успешно добавлены во все таблицы!"