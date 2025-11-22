
# #создание тестовых данных в бд

# from sqlalchemy.ext.asyncio import AsyncSession


# from datetime import datetime, timedelta
# from models.models_bd import (
#     TargetMuscleCategory, User, WorkoutExercises, ProgramsWorkout, 
#     WorkoutExPool, TrainInfo, TrainPool, ApproachesRec, Restrictions
# )

# async def create_test_data(session: AsyncSession):
#     """Создание тестовых данных для всех таблиц"""
    
#     # 1. Target_muscle_category
#     muscle_categories = [
#         # TargetMuscleCategory(id_muscle_category=1, name_muscle_category="Голова"),
#         # TargetMuscleCategory(id_muscle_category=2, name_muscle_category="Руки"),
#         # TargetMuscleCategory(id_muscle_category=3, name_muscle_category="Ноги"),
#         # TargetMuscleCategory(id_muscle_category=4, name_muscle_category="Грудь"),
#         # TargetMuscleCategory(id_muscle_category=5, name_muscle_category="Плечи"),
#         # TargetMuscleCategory(id_muscle_category=6, name_muscle_category="Шея"),
#         # TargetMuscleCategory(id_muscle_category=7, name_muscle_category="Бицепс"),
#         # TargetMuscleCategory(id_muscle_category=8, name_muscle_category="Трицепс"),
#         # TargetMuscleCategory(id_muscle_category=9, name_muscle_category="Квадрицепс"),
#         # TargetMuscleCategory(id_muscle_category=10, name_muscle_category="Трапеции"),
#         # TargetMuscleCategory(id_muscle_category=11, name_muscle_category="Пресс"),
#         # TargetMuscleCategory(id_muscle_category=12, name_muscle_category="Икроножные"),
#         # TargetMuscleCategory(id_muscle_category=13, name_muscle_category="Широкие бедра"),
#         # TargetMuscleCategory(id_muscle_category=14, name_muscle_category="Бицепс бедра"),
#         # TargetMuscleCategory(id_muscle_category=15, name_muscle_category="Косые мышцы живота"),
#         # TargetMuscleCategory(id_muscle_category=16, name_muscle_category="Широчайшие"),
#         # TargetMuscleCategory(id_muscle_category=17, name_muscle_category="Круглые мышцы"),
#         # TargetMuscleCategory(id_muscle_category=18, name_muscle_category="Ягодицы"),
#         # TargetMuscleCategory(id_muscle_category=19, name_muscle_category="Спина")
# #         muscle_mapping = {
# #     1: "Голова",
# #     2: "Руки", 
# #     3: "Ноги",
# #     4: "Грудь",
# #     5: "Плечи",
# #     6: "Шея",
# #     7: "Бицепс",
# #     8: "Трицепс",
# #     9: "Квадрицепс",
# #     10: "Трапеции",
# #     11: "Пресс",
# #     12: "Икроножные",
# #     13: "Широкие бедра",
# #     14: "Бицепс бедра",
# #     15: "Косые мышцы живота",
# #     16: "Широчайшие",
# #     17: "Круглые мышцы",
# #     18: "Ягодичные"
#         TargetMuscleCategory(id_muscle_category=1, name_muscle_category="Бицепс"),
#         TargetMuscleCategory(id_muscle_category=2, name_muscle_category="Трицепс"),
#         TargetMuscleCategory(id_muscle_category=3, name_muscle_category="Грудь"),
#         TargetMuscleCategory(id_muscle_category=4, name_muscle_category="Спина"),
#         TargetMuscleCategory(id_muscle_category=5, name_muscle_category="Ноги"),
#         TargetMuscleCategory(id_muscle_category=6, name_muscle_category="Плечи"),
#         TargetMuscleCategory(id_muscle_category=7, name_muscle_category="Пресс"),
#         TargetMuscleCategory(id_muscle_category=8, name_muscle_category="Трапеция"),        
#         TargetMuscleCategory(id_muscle_category=9, name_muscle_category="Ягодицы"),
#         TargetMuscleCategory(id_muscle_category=10, name_muscle_category="Икры")

#     ]
#     session.add_all(muscle_categories)
#     await session.flush()
    
#     # 2. User (3 пользователя)
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
#         )
#     ]
#     session.add_all(users)
#     await session.flush()
    
#     # 3. Workout_exercises (больше упражнений для разнообразия)
#     workout_exercises = [
    
#     # Упражнения для ног (5)
#     WorkoutExercises(name_workout_exercises="Приседания", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Жим ногами", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Выпады", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Сгибание ног лежа", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
    
#     # Упражнения для груди (3)
#     WorkoutExercises(name_workout_exercises="Жим лежа", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Жим гантелей на наклонной скамье", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Разведение гантелей", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Отжимания на брусьях", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
    
#     # Упражнения для спины (4)
#     WorkoutExercises(name_workout_exercises="Становая тяга", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Подтягивания", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Тяга штанги в наклоне", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Тяга верхнего блока", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
    
#     # Упражнения для плеч (6)
#     WorkoutExercises(name_workout_exercises="Армейский жим", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=6, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Махи гантелями в стороны", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=6, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Тяга штанги к подбородку", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=6, gif_file_workout_exercises=None, vision_user=True),
    
#     # Упражнения для бицепса (1)
#     WorkoutExercises(name_workout_exercises="Подъем штанги на бицепс", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Подъем гантелей на бицепс", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Молотки", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
    
#     # Упражнения для трицепса (2)
#     WorkoutExercises(name_workout_exercises="Французский жим", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Жим лежа узким хватом", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Разгибание на блоке", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
    
#     # Упражнения для пресса (7)
#     WorkoutExercises(name_workout_exercises="Скручивания", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=7, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Подъем ног в висе", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=7, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Планка", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=7, gif_file_workout_exercises=None, vision_user=True),
    
#     # Упражнения для икр (10)
#     WorkoutExercises(name_workout_exercises="Подъемы на носки стоя", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=10, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Подъемы на носки сидя", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=10, gif_file_workout_exercises=None, vision_user=True),
    
#     # Упражнения для ягодиц (9)
#     WorkoutExercises(name_workout_exercises="Ягодичный мост", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=9, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Махи ногой назад", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=9, gif_file_workout_exercises=None, vision_user=True),
    
#     # Упражнения для трапеций (8)
#     WorkoutExercises(name_workout_exercises="Шраги с гантелями", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=8, gif_file_workout_exercises=None, vision_user=True),
    
#     WorkoutExercises(name_workout_exercises="Шраги со штангой", id_creation_user=1, 
#                     notice_workout_exercises=None, 
#                     id_muscle_category=8, gif_file_workout_exercises=None, vision_user=True),
    
# ]

    
#     session.add_all(workout_exercises)
#     await session.flush()
    
#     # 4. Programs_workout (по 2-3 программы на пользователя)
#     programs_workout = [
#         # Программы для пользователя 1001
#         ProgramsWorkout(id_programs_workout=3001, name_programs_workout="Силовая тренировка груди", id_user=1001, week_day_programs_workout="Понедельник"),
#         ProgramsWorkout(id_programs_workout=3002, name_programs_workout="Тренировка спины", id_user=1001, week_day_programs_workout="Среда"),
#         ProgramsWorkout(id_programs_workout=3003, name_programs_workout="Тренировка ног", id_user=1001, week_day_programs_workout="Пятница"),
        
#         # Программы для пользователя 1002
#         ProgramsWorkout(id_programs_workout=3004, name_programs_workout="Верх тела", id_user=1002, week_day_programs_workout="Понедельник"),
#         ProgramsWorkout(id_programs_workout=3005, name_programs_workout="Низ тела", id_user=1002, week_day_programs_workout="Среда"),
#         ProgramsWorkout(id_programs_workout=3006, name_programs_workout="Кардио", id_user=1002, week_day_programs_workout="Пятница"),
        
#         # Программы для пользователя 1003
#         ProgramsWorkout(id_programs_workout=3007, name_programs_workout="Фуллбади", id_user=1003, week_day_programs_workout="Понедельник"),
#         ProgramsWorkout(id_programs_workout=3008, name_programs_workout="Спина-бицепс", id_user=1003, week_day_programs_workout="Среда"),
#     ]
#     session.add_all(programs_workout)
#     await session.flush()
    
#     # 5. Workout_ex_pool (по 3 упражнения на программу)
#     workout_ex_pool = []
#     ex_pool_id = 4001
    
#     # Программа 3001 (Грудь) - 3 упражнения
#     workout_ex_pool.extend([
#         WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3001, id_workout_exercises=2001, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=50),
#         WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3001, id_workout_exercises=2002, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=20),
#         WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3001, id_workout_exercises=2003, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=4, weight_ex_pool=15),
#     ])
#     ex_pool_id += 3
    
#     # Программа 3002 (Спина) - 3 упражнения
#     workout_ex_pool.extend([
#         WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3002, id_workout_exercises=2004, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=40),
#         WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3002, id_workout_exercises=2005, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=6, approaches_target_ex_pool=3, weight_ex_pool=60),
#         WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3002, id_workout_exercises=2006, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=4, weight_ex_pool=25),
#     ])
#     ex_pool_id += 3
    
#     # Программа 3003 (Ноги) - 3 упражнения
#     workout_ex_pool.extend([
#         WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3003, id_workout_exercises=2007, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=6, approaches_target_ex_pool=5, weight_ex_pool=80),
#         WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3003, id_workout_exercises=2008, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=100),
#         WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3003, id_workout_exercises=2009, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=15),
#     ])
#     ex_pool_id += 3
    
#     # Программа 3004 (Верх тела) - 3 упражнения
#     workout_ex_pool.extend([
#         WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3004, id_workout_exercises=2001, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=45),
#         WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3004, id_workout_exercises=2004, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=35),
#         WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3004, id_workout_exercises=2010, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=18),
#     ])
#     ex_pool_id += 3
    
#     # Программа 3005 (Низ тела) - 3 упражнения
#     workout_ex_pool.extend([
#         WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3005, id_workout_exercises=2007, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=5, weight_ex_pool=70),
#         WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3005, id_workout_exercises=2008, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=90),
#         WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3005, id_workout_exercises=2009, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=12),
#     ])
#     ex_pool_id += 3
    
#     # Программа 3006 (Кардио) - 3 упражнения
#     workout_ex_pool.extend([
#         WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3006, id_workout_exercises=2007, max_target_iteration_ex_pool=20, min_target_iteration_ex_pool=15, approaches_target_ex_pool=3, weight_ex_pool=50),
#         WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3006, id_workout_exercises=2009, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=10),
#         WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3006, id_workout_exercises=2011, max_target_iteration_ex_pool=20, min_target_iteration_ex_pool=15, approaches_target_ex_pool=3, weight_ex_pool=8),
#     ])
#     ex_pool_id += 3
    
#     # Программа 3007 (Фуллбади) - 3 упражнения
#     workout_ex_pool.extend([
#         WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3007, id_workout_exercises=2001, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=6, approaches_target_ex_pool=4, weight_ex_pool=55),
#         WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3007, id_workout_exercises=2005, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=3, weight_ex_pool=65),
#         WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3007, id_workout_exercises=2007, max_target_iteration_ex_pool=8, min_target_iteration_ex_pool=5, approaches_target_ex_pool=5, weight_ex_pool=85),
#     ])
#     ex_pool_id += 3
    
#     # Программа 3008 (Спина-бицепс) - 3 упражнения
#     workout_ex_pool.extend([
#         WorkoutExPool(id_ex_pool=ex_pool_id, id_programs_workout=3008, id_workout_exercises=2004, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=4, weight_ex_pool=38),
#         WorkoutExPool(id_ex_pool=ex_pool_id+1, id_programs_workout=3008, id_workout_exercises=2006, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=3, weight_ex_pool=22),
#         WorkoutExPool(id_ex_pool=ex_pool_id+2, id_programs_workout=3008, id_workout_exercises=2012, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=30),
#     ])
    
#     session.add_all(workout_ex_pool)
#     await session.flush()
    
#     # 6. Train_info (по 3-5 тренировок на пользователя)
#     train_info = []
#     train_info_id = 5001
    
#     # Тренировки для пользователя 1001 (5 тренировок)
#     for i in range(5):
#         train_info.append(TrainInfo(
#             id_train_info=train_info_id,
#             datetime_start_train_info=datetime.now() - timedelta(days=7-i),
#             datetime_end_train_info=datetime.now() - timedelta(days=7-i, hours=1, minutes=30),
#             check_train_info=True,
#             Id_user=1001,
#             name_programs_workout=["Силовая тренировка груди", "Тренировка спины", "Тренировка ног"][i % 3]
#         ))
#         train_info_id += 1
    
#     # Тренировки для пользователя 1002 (4 тренировки)
#     for i in range(4):
#         train_info.append(TrainInfo(
#             id_train_info=train_info_id,
#             datetime_start_train_info=datetime.now() - timedelta(days=5-i),
#             datetime_end_train_info=datetime.now() - timedelta(days=5-i, hours=1, minutes=15),
#             check_train_info=True,
#             Id_user=1002,
#             name_programs_workout=["Верх тела", "Низ тела", "Кардио"][i % 3]
#         ))
#         train_info_id += 1
    
#     # Тренировки для пользователя 1003 (3 тренировки)
#     for i in range(3):
#         train_info.append(TrainInfo(
#             id_train_info=train_info_id,
#             datetime_start_train_info=datetime.now() - timedelta(days=3-i),
#             datetime_end_train_info=datetime.now() - timedelta(days=3-i, hours=1, minutes=45),
#             check_train_info=True,
#             Id_user=1003,
#             name_programs_workout=["Фуллбади", "Спина-бицепс"][i % 2]
#         ))
#         train_info_id += 1
    
#     session.add_all(train_info)
#     await session.flush()
    
#     # 7. Train_pool (по 3-4 упражнения на тренировку)
#     train_pool = []
#     train_pool_id = 6001
    
#     # Для каждой тренировки создаем по 3-4 упражнения
#     for train in train_info:
#         num_exercises = 3 if train.id_train_info % 2 == 0 else 4
        
#         # Выбираем случайные упражнения из соответствующих программ
#         program_exercises = [ex for ex in workout_ex_pool if ex.id_programs_workout in [
#             pw.id_programs_workout for pw in programs_workout 
#             if pw.name_programs_workout == train.name_programs_workout
#         ]]
        
#         selected_exercises = program_exercises[:num_exercises]
        
#         for ex in selected_exercises:
#             train_pool.append(TrainPool(
#                 id_train_pool=train_pool_id,
#                 id_train_info=train.id_train_info,
#                 record_bool=(train_pool_id % 3 == 0),  # Каждая третья запись - рекорд
#                 id_workout_exercises=ex.id_workout_exercises
#             ))
#             train_pool_id += 1
    
#     session.add_all(train_pool)
#     await session.flush()
    
#     # 8. Approaches_rec (по 3-4 подхода на упражнение)
#     approaches_rec = []
#     approach_id = 7001
    
#     for train_pool_item in train_pool:
#         num_approaches = 3 if approach_id % 2 == 0 else 4
        
#         for approach_num in range(num_approaches):
#             weight = train_pool_item.id_workout_exercises * 2 + approach_num * 5  # Простая логика веса
#             iterations = 8 + approach_num * 2  # Простая логика повторений
            
#             approaches_rec.append(ApproachesRec(
#                 id_approaches_rec=approach_id,
#                 weight_approaches_rec=weight,
#                 rest_time_up_approaches_rec=datetime.now() - timedelta(minutes=(10 + approach_num)),
#                 rest_time_down_approaches_rec=datetime.now() - timedelta(minutes=(9 + approach_num)),
#                 num_iteration_approaches_rec=iterations,
#                 id_train_pool=train_pool_item.id_train_pool
#             ))
#             approach_id += 1
    
#     session.add_all(approaches_rec)
#     await session.flush()
    
#     # 9. Restrictions (по 1-2 ограничения на пользователя)
#     restrictions = [
#         Restrictions(id_restrictions=8001, id_workout_exercises=2007, id_user=1001),  # Иван - проблемы с приседаниями
#         Restrictions(id_restrictions=8002, id_workout_exercises=2001, id_user=1002),  # Мария - проблемы с жимом
#         Restrictions(id_restrictions=8003, id_workout_exercises=2004, id_user=1002),  # Мария - проблемы с тягой
#         Restrictions(id_restrictions=8004, id_workout_exercises=2008, id_user=1003),  # Алексей - проблемы с жимом ногами
#     ]
#     session.add_all(restrictions)
    
#     # Фиксируем все изменения
#     await session.commit()
#     return "✅ Тестовые данные успешно добавлены во все таблицы!"



#создание тестовых данных в бд

from sqlalchemy.ext.asyncio import AsyncSession


from datetime import datetime, timedelta
from models.models_bd import (
    TargetMuscleCategory, User, WorkoutExercises, ProgramsWorkout, 
    WorkoutExPool, TrainInfo, TrainPool, ApproachesRec, Restrictions
)

async def create_test_data(session: AsyncSession):
    """Создание тестовых данных для всех таблиц"""
    
    # 1. Target_muscle_category
    muscle_categories = [
        
        TargetMuscleCategory(id_muscle_category=1, name_muscle_category="Бицепс"),
        TargetMuscleCategory(id_muscle_category=2, name_muscle_category="Трицепс"),
        TargetMuscleCategory(id_muscle_category=3, name_muscle_category="Грудь"),
        TargetMuscleCategory(id_muscle_category=4, name_muscle_category="Спина"),
        TargetMuscleCategory(id_muscle_category=5, name_muscle_category="Ноги"),
        TargetMuscleCategory(id_muscle_category=6, name_muscle_category="Плечи"),
        TargetMuscleCategory(id_muscle_category=7, name_muscle_category="Пресс"),
        TargetMuscleCategory(id_muscle_category=8, name_muscle_category="Трапеция"),        
        TargetMuscleCategory(id_muscle_category=9, name_muscle_category="Ягодицы"),
        TargetMuscleCategory(id_muscle_category=10, name_muscle_category="Икры")

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
    
    # 3. Workout_exercises
    workout_exercises = [
        # Упражнения для ног (5)
        WorkoutExercises(name_workout_exercises="Приседания", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Жим ногами", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Выпады", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Сгибание ног лежа", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для груди (3)
        WorkoutExercises(name_workout_exercises="Жим лежа", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Жим гантелей на наклонной скамье", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Разведение гантелей", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Отжимания на брусьях", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для спины (4)
        WorkoutExercises(name_workout_exercises="Становая тяга", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Подтягивания", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Тяга штанги в наклоне", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Тяга верхнего блока", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для плеч (6)
        WorkoutExercises(name_workout_exercises="Армейский жим", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=6, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Махи гантелями в стороны", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=6, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Тяга штанги к подбородку", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=6, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для бицепса (1)
        WorkoutExercises(name_workout_exercises="Подъем штанги на бицепс", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Подъем гантелей на бицепс", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Молотки", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для трицепса (2)
        WorkoutExercises(name_workout_exercises="Французский жим", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Жим лежа узким хватом", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Разгибание на блоке", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для пресса (7)
        WorkoutExercises(name_workout_exercises="Скручивания", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=7, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Подъем ног в висе", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=7, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Планка", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=7, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для икр (10)
        WorkoutExercises(name_workout_exercises="Подъемы на носки стоя", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=10, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Подъемы на носки сидя", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=10, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для ягодиц (9)
        WorkoutExercises(name_workout_exercises="Ягодичный мост", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=9, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Махи ногой назад", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=9, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для трапеций (8)
        WorkoutExercises(name_workout_exercises="Шраги с гантелями", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=8, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(name_workout_exercises="Шраги со штангой", id_creation_user=1, 
                        notice_workout_exercises=None, 
                        id_muscle_category=8, gif_file_workout_exercises=None, vision_user=True),
    ]

    session.add_all(workout_exercises)
    await session.flush()
    
    # 4. Programs_workout (по 2-3 программы на пользователя)
    programs_workout = [
        # Программы для пользователя 1001
        ProgramsWorkout(name_programs_workout="Силовая тренировка груди", id_user=1001, week_day_programs_workout="Понедельник"),
        ProgramsWorkout(name_programs_workout="Тренировка спины", id_user=1001, week_day_programs_workout="Среда"),
        ProgramsWorkout(name_programs_workout="Тренировка ног", id_user=1001, week_day_programs_workout="Пятница"),
        
        # Программы для пользователя 1002
        ProgramsWorkout(name_programs_workout="Верх тела", id_user=1002, week_day_programs_workout="Понедельник"),
        ProgramsWorkout(name_programs_workout="Низ тела", id_user=1002, week_day_programs_workout="Среда"),
        ProgramsWorkout(name_programs_workout="Кардио", id_user=1002, week_day_programs_workout="Пятница"),
        
        # Программы для пользователя 1003
        ProgramsWorkout(name_programs_workout="Фуллбади", id_user=1003, week_day_programs_workout="Понедельник"),
        ProgramsWorkout(name_programs_workout="Спина-бицепс", id_user=1003, week_day_programs_workout="Среда"),
    ]
    session.add_all(programs_workout)
    await session.flush()
    
    # 5. Workout_ex_pool (по 3 упражнения на программу)
    workout_ex_pool = []
    
    # Программа 1 (Грудь) - 4 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_programs_workout=programs_workout[0].id_programs_workout, id_workout_exercises=workout_exercises[4].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=50),  # Жим лежа
        WorkoutExPool(id_programs_workout=programs_workout[0].id_programs_workout, id_workout_exercises=workout_exercises[5].id_workout_exercises, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=20),  # Жим гантелей на наклонной
        WorkoutExPool(id_programs_workout=programs_workout[0].id_programs_workout, id_workout_exercises=workout_exercises[6].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=4, weight_ex_pool=15),  # Разведение гантелей
        WorkoutExPool(id_programs_workout=programs_workout[0].id_programs_workout, id_workout_exercises=workout_exercises[7].id_workout_exercises, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=8, approaches_target_ex_pool=3, weight_ex_pool=0),   # Отжимания на брусьях
    ])
    
    # Программа 2 (Спина) - 4 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_programs_workout=programs_workout[1].id_programs_workout, id_workout_exercises=workout_exercises[8].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=40),  # Становая тяга
        WorkoutExPool(id_programs_workout=programs_workout[1].id_programs_workout, id_workout_exercises=workout_exercises[9].id_workout_exercises, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=6, approaches_target_ex_pool=3, weight_ex_pool=0),   # Подтягивания
        WorkoutExPool(id_programs_workout=programs_workout[1].id_programs_workout, id_workout_exercises=workout_exercises[10].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=4, weight_ex_pool=25), # Тяга штанги в наклоне
        WorkoutExPool(id_programs_workout=programs_workout[1].id_programs_workout, id_workout_exercises=workout_exercises[11].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=35), # Тяга верхнего блока
    ])
    
    # Программа 3 (Ноги) - 4 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_programs_workout=programs_workout[2].id_programs_workout, id_workout_exercises=workout_exercises[0].id_workout_exercises, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=6, approaches_target_ex_pool=5, weight_ex_pool=80),   # Приседания
        WorkoutExPool(id_programs_workout=programs_workout[2].id_programs_workout, id_workout_exercises=workout_exercises[1].id_workout_exercises, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=100), # Жим ногами
        WorkoutExPool(id_programs_workout=programs_workout[2].id_programs_workout, id_workout_exercises=workout_exercises[2].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=15),  # Выпады
        WorkoutExPool(id_programs_workout=programs_workout[2].id_programs_workout, id_workout_exercises=workout_exercises[3].id_workout_exercises, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=25),  # Сгибание ног лежа
    ])
    
    # Программа 4 (Верх тела) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_programs_workout=programs_workout[3].id_programs_workout, id_workout_exercises=workout_exercises[4].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=45),  # Жим лежа
        WorkoutExPool(id_programs_workout=programs_workout[3].id_programs_workout, id_workout_exercises=workout_exercises[8].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=35), # Становая тяга
        WorkoutExPool(id_programs_workout=programs_workout[3].id_programs_workout, id_workout_exercises=workout_exercises[12].id_workout_exercises, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=18), # Армейский жим
    ])
    
    # Программа 5 (Низ тела) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_programs_workout=programs_workout[4].id_programs_workout, id_workout_exercises=workout_exercises[0].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=5, weight_ex_pool=70),   # Приседания
        WorkoutExPool(id_programs_workout=programs_workout[4].id_programs_workout, id_workout_exercises=workout_exercises[1].id_workout_exercises, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=90), # Жим ногами
        WorkoutExPool(id_programs_workout=programs_workout[4].id_programs_workout, id_workout_exercises=workout_exercises[2].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=3, weight_ex_pool=12),  # Выпады
    ])
    
    # Программа 6 (Кардио) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_programs_workout=programs_workout[5].id_programs_workout, id_workout_exercises=workout_exercises[0].id_workout_exercises, max_target_iteration_ex_pool=20, min_target_iteration_ex_pool=15, approaches_target_ex_pool=3, weight_ex_pool=50),   # Приседания
        WorkoutExPool(id_programs_workout=programs_workout[5].id_programs_workout, id_workout_exercises=workout_exercises[2].id_workout_exercises, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=4, weight_ex_pool=10),  # Выпады
        WorkoutExPool(id_programs_workout=programs_workout[5].id_programs_workout, id_workout_exercises=workout_exercises[21].id_workout_exercises, max_target_iteration_ex_pool=20, min_target_iteration_ex_pool=15, approaches_target_ex_pool=3, weight_ex_pool=8),  # Подъемы на носки стоя
    ])
    
    # Программа 7 (Фуллбади) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_programs_workout=programs_workout[6].id_programs_workout, id_workout_exercises=workout_exercises[4].id_workout_exercises, max_target_iteration_ex_pool=10, min_target_iteration_ex_pool=6, approaches_target_ex_pool=4, weight_ex_pool=55),  # Жим лежа
        WorkoutExPool(id_programs_workout=programs_workout[6].id_programs_workout, id_workout_exercises=workout_exercises[8].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=3, weight_ex_pool=65),  # Становая тяга
        WorkoutExPool(id_programs_workout=programs_workout[6].id_programs_workout, id_workout_exercises=workout_exercises[0].id_workout_exercises, max_target_iteration_ex_pool=8, min_target_iteration_ex_pool=5, approaches_target_ex_pool=5, weight_ex_pool=85),   # Приседания
    ])
    
    # Программа 8 (Спина-бицепс) - 3 упражнения
    workout_ex_pool.extend([
        WorkoutExPool(id_programs_workout=programs_workout[7].id_programs_workout, id_workout_exercises=workout_exercises[10].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=10, approaches_target_ex_pool=4, weight_ex_pool=38), # Тяга штанги в наклоне
        WorkoutExPool(id_programs_workout=programs_workout[7].id_programs_workout, id_workout_exercises=workout_exercises[11].id_workout_exercises, max_target_iteration_ex_pool=15, min_target_iteration_ex_pool=12, approaches_target_ex_pool=3, weight_ex_pool=22), # Тяга верхнего блока
        WorkoutExPool(id_programs_workout=programs_workout[7].id_programs_workout, id_workout_exercises=workout_exercises[15].id_workout_exercises, max_target_iteration_ex_pool=12, min_target_iteration_ex_pool=8, approaches_target_ex_pool=4, weight_ex_pool=30), # Подъем штанги на бицепс
    ])
    
    session.add_all(workout_ex_pool)
    await session.flush()
    
    # 6. Train_info (5 выполнений каждой программы ТОЛЬКО для пользователя 1001)
    train_info = []
    
    # Базовый вес для пользователя 1001
    user_base_weight = 40
    
    # Создаем тренировки в правильном хронологическом порядке (от старых к новым)
    current_date = datetime.now()
    
    # ТОЛЬКО для программ пользователя 1001
    user_1001_programs = [program for program in programs_workout if program.id_user == 1001]
    
    for program in user_1001_programs:
        # Создаем 5 выполнений этой программы в разные дни
        for day in range(5):
            # Создаем разные даты для каждой тренировки
            days_ago = 14 - day * 3  # 14, 11, 8, 5, 2 дней назад
            train_date = current_date - timedelta(days=days_ago)
            
            train_info.append(TrainInfo(
                datetime_start_train_info=train_date,
                datetime_end_train_info=train_date + timedelta(hours=1, minutes=30),
                check_train_info=True,
                Id_user=1001,  # Только пользователь 1001
                name_programs_workout=program.name_programs_workout
            ))
    
    session.add_all(train_info)
    await session.flush()
    
    # 7. Train_pool (упражнения для тренировок ТОЛЬКО пользователя 1001)
    train_pool = []
    
    for train in train_info:
        program = next((pw for pw in programs_workout 
                       if pw.name_programs_workout == train.name_programs_workout 
                       and pw.id_user == train.Id_user), None)
        
        if program:
            program_exercises = [ex for ex in workout_ex_pool 
                               if ex.id_programs_workout == program.id_programs_workout]
            
            for ex in program_exercises:
                train_pool.append(TrainPool(
                    id_train_info=train.id_train_info,
                    record_bool=False,
                    id_workout_exercises=ex.id_workout_exercises
                ))
    
    session.add_all(train_pool)
    await session.flush()
    
    # 8. Approaches_rec (подходы ТОЛЬКО для пользователя 1001)
    approaches_rec = []
    
    # Группируем тренировки по программам пользователя 1001 и сортируем по дате
    program_trainings = {}
    for train in train_info:
        key = (train.Id_user, train.name_programs_workout)
        if key not in program_trainings:
            program_trainings[key] = []
        program_trainings[key].append(train)
    
    # Сортируем тренировки внутри каждой программы по дате (от старых к новым)
    for key in program_trainings:
        program_trainings[key].sort(key=lambda x: x.datetime_start_train_info)
    
    for train_pool_item in train_pool:
        train = next((t for t in train_info if t.id_train_info == train_pool_item.id_train_info), None)
        
        if train:
            key = (train.Id_user, train.name_programs_workout)
            program_trains = program_trainings.get(key, [])
            
            # Находим индекс этой тренировки в последовательности
            try:
                day_index = program_trains.index(train)
            except ValueError:
                day_index = 0
            
            ex_pool_item = next((ex for ex in workout_ex_pool 
                               if ex.id_workout_exercises == train_pool_item.id_workout_exercises), None)
            
            if ex_pool_item:
                # Правильное увеличение веса: старые тренировки - меньший вес, новые - больший
                day_weight_increase = day_index * 5  # +5 кг с каждой следующей тренировкой
                base_weight = ex_pool_item.weight_ex_pool + day_weight_increase
                base_iterations = ex_pool_item.min_target_iteration_ex_pool
                
                num_approaches = ex_pool_item.approaches_target_ex_pool
                
                for approach_num in range(num_approaches):
                    # Вес одинаковый во всех подходах одной тренировки
                    weight = base_weight
                    
                    # Повторения немного варьируются по подходам
                    iterations = base_iterations - approach_num
                    iterations = max(iterations, 4)
                    
                    approaches_rec.append(ApproachesRec(
                        weight_approaches_rec=weight,
                        rest_time_up_approaches_rec=train.datetime_start_train_info + timedelta(minutes=10 + approach_num),
                        rest_time_down_approaches_rec=train.datetime_start_train_info + timedelta(minutes=9 + approach_num),
                        num_iteration_approaches_rec=iterations,
                        id_train_pool=train_pool_item.id_train_pool
                    ))
    
    session.add_all(approaches_rec)
    await session.flush()
    
    # 9. Restrictions (ограничения для всех пользователей)
    restrictions = [
        Restrictions(id_workout_exercises=workout_exercises[0].id_workout_exercises, id_user=1001),  # Иван - проблемы с приседаниями
        Restrictions(id_workout_exercises=workout_exercises[4].id_workout_exercises, id_user=1002),  # Мария - проблемы с жимом лежа
        Restrictions(id_workout_exercises=workout_exercises[8].id_workout_exercises, id_user=1002),  # Мария - проблемы со становой тягой
        Restrictions(id_workout_exercises=workout_exercises[1].id_workout_exercises, id_user=1003),  # Алексей - проблемы с жимом ногами
    ]
    session.add_all(restrictions)
    
    # Фиксируем все изменения
    await session.commit()
    return "✅ Тестовые данные успешно добавлены во все таблицы!"