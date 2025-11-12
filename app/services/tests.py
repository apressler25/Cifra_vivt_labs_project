
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
        TargetMuscleCategory(id_muscle_category=1, name_muscle_category="Голова"),
        TargetMuscleCategory(id_muscle_category=2, name_muscle_category="Руки"),
        TargetMuscleCategory(id_muscle_category=3, name_muscle_category="Ноги"),
        TargetMuscleCategory(id_muscle_category=4, name_muscle_category="Грудь"),
        TargetMuscleCategory(id_muscle_category=5, name_muscle_category="Плечи"),
        TargetMuscleCategory(id_muscle_category=6, name_muscle_category="Шея"),
        TargetMuscleCategory(id_muscle_category=7, name_muscle_category="Бицепс"),
        TargetMuscleCategory(id_muscle_category=8, name_muscle_category="Трицепс"),
        TargetMuscleCategory(id_muscle_category=9, name_muscle_category="Квадрицепс"),
        TargetMuscleCategory(id_muscle_category=10, name_muscle_category="Трапеции"),
        TargetMuscleCategory(id_muscle_category=11, name_muscle_category="Пресс"),
        TargetMuscleCategory(id_muscle_category=12, name_muscle_category="Икроножные"),
        TargetMuscleCategory(id_muscle_category=13, name_muscle_category="Широкие бедра"),
        TargetMuscleCategory(id_muscle_category=14, name_muscle_category="Бицепс бедра"),
        TargetMuscleCategory(id_muscle_category=15, name_muscle_category="Косые мышцы живота"),
        TargetMuscleCategory(id_muscle_category=16, name_muscle_category="Широчайшие"),
        TargetMuscleCategory(id_muscle_category=17, name_muscle_category="Круглые мышцы"),
        TargetMuscleCategory(id_muscle_category=18, name_muscle_category="Ягодичные")
        
#         muscle_mapping = {
#     1: "Голова",
#     2: "Руки", 
#     3: "Ноги",
#     4: "Грудь",
#     5: "Плечи",
#     6: "Шея",
#     7: "Бицепс",
#     8: "Трицепс",
#     9: "Квадрицепс",
#     10: "Трапеции",
#     11: "Пресс",
#     12: "Икроножные",
#     13: "Широкие бедра",
#     14: "Бицепс бедра",
#     15: "Косые мышцы живота",
#     16: "Широчайшие",
#     17: "Круглые мышцы",
#     18: "Ягодичные"
# }


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
        
        
        # Упражнения для ног (3)
        WorkoutExercises(id_workout_exercises=1, name_workout_exercises="Приседания со штангой", id_creation_user=1, 
                        notice_workout_exercises="Техника: Расположите штангу на трапециях, ноги на ширине плеч. Медленно опускайтесь до параллели бедер с полом, сохраняя спину прямой. Поднимайтесь мощным движением, выдыхая в верхней точке. Колени не должны выходить за носки.", 
                        id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=2, name_workout_exercises="Жим ногами", id_creation_user=1, 
                        notice_workout_exercises="Техника: Сядьте в тренажер, плотно прижмите спину к спинке. Ноги поставьте на платформу на ширине плеч. Медленно опускайте платформу до угла 90 градусов в коленях, затем мощно выжимайте вверх. Не разгибайте колени полностью.", 
                        id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=3, name_workout_exercises="Выпады с гантелями", id_creation_user=1, 
                        notice_workout_exercises="Техника: Возьмите гантели в обе руки. Сделайте шаг вперед, опускаясь до образования двух прямых углов в коленях. Переднее колено не должно выходить за носок. Вернитесь в исходное положение, оттолкнувшись передней ногой.", 
                        id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=4, name_workout_exercises="Сгибание ног лежа", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лягте на тренажер, валики должны располагаться на ахилловых сухожилиях. Плавно сгибайте ноги, поднимая валики к ягодицам. В верхней точке задержитесь на 1-2 секунды, затем медленно опускайте ноги. Не отрывайте таз от скамьи.", 
                        id_muscle_category=3, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для груди (4)
        WorkoutExercises(id_workout_exercises=5, name_workout_exercises="Жим штанги лежа", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лягте на скамью, стопы плотно на полу. Возьмитесь за гриф чуть шире плеч. Опускайте штангу к нижней части груди, локти под углом 45 градусов. Мощно выжмите штангу вверх, полностью выпрямляя руки.", 
                        id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=6, name_workout_exercises="Жим гантелей на наклонной скамье", id_creation_user=1, 
                        notice_workout_exercises="Техника: Установите скамью под углом 30-45 градусов. Возьмите гантели, опустите их к верхней части груди. Локти направлены в стороны под углом 45 градусов. Выжмите гантели вверх по дуге, в верхней точке сведите их вместе.", 
                        id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=7, name_workout_exercises="Разведение гантелей лежа", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лягте на скамью, поднимите гантели над грудью. Медленно разводите руки в стороны, слегка сгибая локти. Опускайте гантели до уровня груди, чувствуя растяжение. Плавно сведите руки в исходное положение.", 
                        id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=8, name_workout_exercises="Отжимания на брусьях", id_creation_user=1, 
                        notice_workout_exercises="Техника: Возьмитесь за брусья, скрестив ноги. Медленно опускайтесь, наклоняя корпус вперед для акцента на грудь. Опускайтесь до угла 90 градусов в локтях. Мощно отожмитесь вверх, выдыхая в верхней точке.", 
                        id_muscle_category=4, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для спины (16 - широчайшие)
        WorkoutExercises(id_workout_exercises=9, name_workout_exercises="Становая тяга", id_creation_user=1, 
                        notice_workout_exercises="Техника: Поставьте ноги на ширине плеч, штанга над стопами. Возьмитесь за гриф прямым хватом. Держа спину прямой, мощно поднимите штангу вдоль ног. В верхней точке сведите лопатки. Медленно опустите штангу по той же траектории.", 
                        id_muscle_category=16, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=10, name_workout_exercises="Подтягивания широким хватом", id_creation_user=1, 
                        notice_workout_exercises="Техника: Возьмитесь за перекладину широким хватом. Сведите лопатки, подтянитесь до уровня подбородка. В верхней точке задержитесь на 1 секунду. Медленно опуститесь в исходное положение. Не раскачивайте корпус.", 
                        id_muscle_category=16, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=11, name_workout_exercises="Тяга штанги в наклоне", id_creation_user=1, 
                        notice_workout_exercises="Техника: Наклоните корпус вперед до параллели с полом. Возьмите штангу прямым хватом. Подтяните штангу к низу живота, сводя лопатки. Локти должны двигаться вдоль тела. Медленно опустите штангу, чувствуя растяжение в спине.", 
                        id_muscle_category=16, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=12, name_workout_exercises="Тяга верхнего блока", id_creation_user=1, 
                        notice_workout_exercises="Техника: Сядьте в тренажер, зафиксируйте бедра. Возьмитесь за рукоять широким хватом. Плавно потяните рукоять к груди, отклоняя корпус назад. Сведите лопатки в нижней точке. Медленно верните рукоять в исходное положение.", 
                        id_muscle_category=16, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для плеч (5)
        WorkoutExercises(id_workout_exercises=13, name_workout_exercises="Армейский жим", id_creation_user=1, 
                        notice_workout_exercises="Техника: Стоя или сидя, поднимите штангу до уровня груди. Ладони чуть шире плеч. Выжмите штангу строго вверх над головой. В верхней точке полностью выпрямите руки. Медленно опустите штангу до ключиц.", 
                        id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=14, name_workout_exercises="Махи гантелями в стороны", id_creation_user=1, 
                        notice_workout_exercises="Техника: Стоя, держите гантели по бокам. Слегка согните локти. Поднимите гантели через стороны до уровня плеч. В верхней точке мизинец должен быть выше большого пальца. Медленно опустите гантели, контролируя движение.", 
                        id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=15, name_workout_exercises="Тяга штанги к подбородку", id_creation_user=1, 
                        notice_workout_exercises="Техника: Возьмите штангу узким хватом. Поднимите локти в стороны, тяните штангу вдоль тела до уровня подбородок. Локти должны быть выше кистей. Медленно опустите штангу в исходное положение. Держите корпус прямым.", 
                        id_muscle_category=5, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для бицепса (7)
        WorkoutExercises(id_workout_exercises=16, name_workout_exercises="Подъем штанги на бицепс", id_creation_user=1, 
                        notice_workout_exercises="Техника: Стоя, возьмите штангу обратным хватом. Локти прижмите к бокам. Поднимите штангу до уровня плеч, сокращая бицепсы. В верхней точке задержитесь на 1 секунду. Медленно опустите штангу, полностью выпрямляя руки.", 
                        id_muscle_category=7, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=17, name_workout_exercises="Подъем гантелей на бицепс", id_creation_user=1, 
                        notice_workout_exercises="Техника: Сидя или стоя, держите гантели нейтральным хватом. Поочередно или одновременно сгибайте руки, разворачивая кисти наружу. В верхней точке максимально сократите бицепсы. Медленно опустите гантели с контролем.", 
                        id_muscle_category=7, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=18, name_workout_exercises="Молотки с гантелями", id_creation_user=1, 
                        notice_workout_exercises="Техника: Держите гантели нейтральным хватом (ладони смотрят друг на друга). Поднимайте гантели к плечам, сохраняя положение кистей. Локти неподвижны вдоль тела. В верхней точке задержитесь, затем медленно опустите.", 
                        id_muscle_category=7, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для трицепса (8)
        WorkoutExercises(id_workout_exercises=19, name_workout_exercises="Французский жим", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лежа на скамье, поднимите штангу над грудью. Медленно опускайте штангу ко лбу, сгибая только локтевые суставы. Локти направлены вверх и немного внутрь. Мощно выпрямите руки, возвращая штангу в исходное положение.", 
                        id_muscle_category=8, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=20, name_workout_exercises="Жим лежа узким хватом", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лягте на скамью, возьмитесь за гриф на ширине плеч. Опускайте штангу к низу груди, локти прижаты к телу. Выжимайте штангу вверх, фокусируясь на работе трицепсов. Не разводите локти в стороны.", 
                        id_muscle_category=8, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=21, name_workout_exercises="Разгибание на блоке", id_creation_user=1, 
                        notice_workout_exercises="Техника: Стоя у блока, возьмитесь за рукоять прямым хватом. Локти прижаты к бокам. Разгибайте руки вниз, полностью выпрямляя их. В нижней точке задержитесь на 1-2 секунды. Медленно верните рукоять в исходное положение.", 
                        id_muscle_category=8, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для пресса (11)
        WorkoutExercises(id_workout_exercises=22, name_workout_exercises="Скручивания на пресс", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лежа на полу, согните ноги в коленях. Руки за головой или скрещены на груди. На выдохе поднимите верхнюю часть туловища, скручивая пресс. Поясница остается на полу. На вдохе медленно опуститесь в исходное положение.", 
                        id_muscle_category=11, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=23, name_workout_exercises="Подъем ног в висе", id_creation_user=1, 
                        notice_workout_exercises="Техника: Повисните на перекладине. Медленно поднимите прямые ноги до параллели с полом или выше. В верхней точке задержитесь на 1-2 секунды. Медленно опустите ноги, не раскачивая корпус. Для усложнения можно поднимать ноги к перекладине.", 
                        id_muscle_category=11, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=24, name_workout_exercises="Планка", id_creation_user=1, 
                        notice_workout_exercises="Техника: Примите упор лежа на предплечьях. Локти под плечами, тело образует прямую линию от головы до пяток. Напрягите пресс и ягодицы, не прогибайтесь в пояснице. Дышите ровно. Удерживайте положение заданное время.", 
                        id_muscle_category=11, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для икр (12)
        WorkoutExercises(id_workout_exercises=25, name_workout_exercises="Подъемы на носки стоя", id_creation_user=1, 
                        notice_workout_exercises="Техника: Встаньте носками на платформу в тренажере, пятки опущены. Поднимитесь на носки как можно выше, напрягая икроножные мышцы. В верхней точке задержитесь на 1-2 секунды. Медленно опустите пятки ниже уровня платформы для растяжения.", 
                        id_muscle_category=12, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=26, name_workout_exercises="Подъемы на носки сидя", id_creation_user=1, 
                        notice_workout_exercises="Техника: Сядьте в тренажер, поставьте носки на платформу. Опустите пятки как можно ниже. Поднимитесь на носки, максимально сокращая камбаловидные мышцы. Задержитесь в верхней точке. Медленно вернитесь в исходное положение.", 
                        id_muscle_category=12, gif_file_workout_exercises=None, vision_user=True),
        
        # Упражнения для ягодиц (18)
        WorkoutExercises(id_workout_exercises=27, name_workout_exercises="Ягодичный мост", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лежа на спине, согните ноги, стопы на полу. Поднимите таз вверх, сжимая ягодицы. В верхней точке тело должно образовать прямую линию от плеч до колен. Задержитесь на 2-3 секунды. Медленно опустите таз, не касаясь пола.", 
                        id_muscle_category=18, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=28, name_workout_exercises="Махи ногой назад", id_creation_user=1, 
                        notice_workout_exercises="Техника: Стоя на четвереньках. Поднимите согнутую ногу назад и вверх, максимально сокращая ягодичную мышцу. В верхней точке задержитесь на 1-2 секунды. Медленно верните ногу в исходное положение. Не прогибайте поясницу.", 
                        id_muscle_category=18, gif_file_workout_exercises=None, vision_user=True),
        
        
        
        
        
            # Упражнения для головы (1) - мышцы шеи и лица
        WorkoutExercises(id_workout_exercises=29, name_workout_exercises="Жим штанги с подъемом головы", id_creation_user=1, 
                        notice_workout_exercises="Техника: Выполняя жим штанги стоя или сидя, сознательно напрягайте мышцы шеи и поддерживайте правильное положение головы. Это укрепляет глубокие мышцы шеи и улучшает осанку при работе с весами.",
                        id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=30, name_workout_exercises="Тяга к подбородку с напряжением шеи", id_creation_user=1, 
                        notice_workout_exercises="Техника: При выполнении тяги штанги к подбородку сохраняйте шею в нейтральном положении, напрягая мышцы для стабилизации. Локти поднимайте выше уровня плеч для комплексной нагрузки.",
                        id_muscle_category=1, gif_file_workout_exercises=None, vision_user=True),

        # Упражнения для рук (2) - комплексные
        WorkoutExercises(id_workout_exercises=31, name_workout_exercises="Подъем штанги на бицепс с супинацией", id_creation_user=1, 
                        notice_workout_exercises="Техника: Возьмите штангу обратным хватом. При подъеме разворачивайте кисти наружу (супинация). В верхней точке максимально сокращайте бицепсы. Медленно опускайте с контролем.",
                        id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=32, name_workout_exercises="Молотковые сгибания с гантелями", id_creation_user=1, 
                        notice_workout_exercises="Техника: Держите гантели нейтральным хватом. Поднимайте гантели к плечам, сохраняя положение ладоней. Локти прижаты к корпусу. Упражнение развивает плечевую и плече-лучевую мышцы.",
                        id_muscle_category=2, gif_file_workout_exercises=None, vision_user=True),

        # Упражнения для шеи (6)
        WorkoutExercises(id_workout_exercises=33, name_workout_exercises="Шраги со штангой за спиной", id_creation_user=1, 
                        notice_workout_exercises="Техника: Возьмите штангу за спиной прямым хватом. Поднимайте плечи вертикально вверх, максимально сокращая трапеции и мышцы шеи. Задержитесь в верхней точке на 2 секунды.",
                        id_muscle_category=6, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=34, name_workout_exercises="Тяга лица на блоке", id_creation_user=1, 
                        notice_workout_exercises="Техника: Установите тросовый блок на уровне лица. Возьмитесь за канатную рукоять, тяните ее к лицу, разводя руки в стороны. Локти высоко, лопатки сведены. Укрепляет задние дельты и мышцы шеи.",
                        id_muscle_category=6, gif_file_workout_exercises=None, vision_user=True),

        # Упражнения для квадрицепса (9)
        WorkoutExercises(id_workout_exercises=35, name_workout_exercises="Приседания в тренажере Смита", id_creation_user=1, 
                        notice_workout_exercises="Техника: Встаньте в тренажер Смита, штанга на трапециях. Выполняйте приседания, концентрируясь на работе квадрицепсов. Опускайтесь до параллели, мощно поднимайтесь вверх.",
                        id_muscle_category=9, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=36, name_workout_exercises="Жим ногами с узкой постановкой", id_creation_user=1, 
                        notice_workout_exercises="Техника: В тренажере для жима ногами поставьте стопы близко друг к другу в нижней части платформы. Это смещает нагрузку на квадрицепсы. Выполняйте жим с полной амплитудой.",
                        id_muscle_category=9, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=37, name_workout_exercises="Выпады в тренажере Смита", id_creation_user=1, 
                        notice_workout_exercises="Техника: Поместите штангу в тренажере Смита на плечи. Выполняйте выпады вперед, сохраняя равновесие. Переднее колено не выходит за носок. Чередуйте ноги.",
                        id_muscle_category=9, gif_file_workout_exercises=None, vision_user=True),

        # Упражнения для трапеций (10)
        WorkoutExercises(id_workout_exercises=38, name_workout_exercises="Шраги со штангой", id_creation_user=1, 
                        notice_workout_exercises="Техника: Стоя прямо, держите штангу перед бедрами. Поднимайте плечи как можно выше к ушам. В верхней точке задержитесь на 2-3 секунды. Опускайте медленно с контролем.",
                        id_muscle_category=10, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=39, name_workout_exercises="Шраги с гантелями", id_creation_user=1, 
                        notice_workout_exercises="Техника: Держите гантели по бокам. Выполняйте вертикальные подъемы плеч. Можно добавить круговые движения плечами для комплексной проработки всех пучков трапеций.",
                        id_muscle_category=10, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=40, name_workout_exercises="Тяга штанги к подбородку широким хватом", id_creation_user=1, 
                        notice_workout_exercises="Техника: Возьмите штангу широким хватом. Поднимайте локти в стороны, тяните штангу вдоль тела до уровня груди. Акцент на трапеции и дельты. Медленно опускайте.",
                        id_muscle_category=10, gif_file_workout_exercises=None, vision_user=True),

        # Упражнения для широких бедер (13)
        WorkoutExercises(id_workout_exercises=41, name_workout_exercises="Приседания сумо", id_creation_user=1, 
                        notice_workout_exercises="Техника: Поставьте ноги значительно шире плеч, носки развернуты наружу. Опускайтесь в присед, сохраняя спину прямой. Колени направлены в стороны. Мощно поднимайтесь.",
                        id_muscle_category=13, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=42, name_workout_exercises="Сведения ног в тренажере", id_creation_user=1, 
                        notice_workout_exercises="Техника: Сядьте в тренажер, установите comfortable вес. Сводите бедра, преодолевая сопротивление. В точке максимального сведения задержитесь на 1-2 секунды. Медленно возвращайтесь.",
                        id_muscle_category=13, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=43, name_workout_exercises="Боковые выпады с гантелями", id_creation_user=1, 
                        notice_workout_exercises="Техника: Держите гантели в обеих руках. Сделайте широкий шаг в сторону, опускаясь на согнутую ногу. Вторая нога прямая. Возвращайтесь в исходное положение мощным движением.",
                        id_muscle_category=13, gif_file_workout_exercises=None, vision_user=True),

        # Упражнения для бицепса бедра (14)
        WorkoutExercises(id_workout_exercises=44, name_workout_exercises="Румынская тяга со штангой", id_creation_user=1, 
                        notice_workout_exercises="Техника: Держите штангу перед бедрами. Наклоняйтесь вперед, отводя таз назад. Опускайте штангу до середины голеней. Чувствуйте растяжение в бицепсах бедер. Возвращайтесь за счет силы задней поверхности.",
                        id_muscle_category=14, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=45, name_workout_exercises="Сгибания ног лежа", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лягте на тренажер лицом вниз, валики на ахилловых сухожилиях. Сгибайте ноги, поднимая валики к ягодицам. В верхней точке максимально сократите бицепсы бедер. Медленно опускайте.",
                        id_muscle_category=14, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=46, name_workout_exercises="Гудмонинги (Good Mornings)", id_creation_user=1, 
                        notice_workout_exercises="Техника: Положите штангу на трапеции как при приседаниях. Наклоняйтесь вперед с прямой спиной до параллели с полом. Возвращайтесь в исходное положение за счет бицепсов бедер.",
                        id_muscle_category=14, gif_file_workout_exercises=None, vision_user=True),

        # Упражнения для косых мышц живота (15)
        WorkoutExercises(id_workout_exercises=47, name_workout_exercises="Боковые скручивания на римском стуле", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лягте на римский стул боком. Руки за головой. Поднимайте корпус вбок, сокращая косые мышцы. Выполняйте медленно с полным контролем. Чередуйте стороны.",
                        id_muscle_category=15, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=48, name_workout_exercises="Русские скручивания с диском", id_creation_user=1, 
                        notice_workout_exercises="Техника: Сядьте на пол, отклоните корпус назад, ноги подняты. Держите диск перед собой. Поворачивайте корпус с диском из стороны в стороны. Держите пресс напряженным.",
                        id_muscle_category=15, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=49, name_workout_exercises="Боковые наклоны с гантелью", id_creation_user=1, 
                        notice_workout_exercises="Техника: Стоя прямо, держите гантель в одной руке. Наклоняйтесь в противоположную сторону, чувствуя растяжение косых мышц. Возвращайтесь в исходное положение. Чередуйте стороны.",
                        id_muscle_category=15, gif_file_workout_exercises=None, vision_user=True),

        # Упражнения для круглых мышц (17)
        WorkoutExercises(id_workout_exercises=50, name_workout_exercises="Тяга гантели в наклоне", id_creation_user=1, 
                        notice_workout_exercises="Техника: Упритесь коленом и рукой в скамью. Возьмите гантель, подтяните ее к поясу. Локоть направлен вверх. В верхней точке максимально сведите лопатку. Медленно опустите.",
                        id_muscle_category=17, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=51, name_workout_exercises="Тяга Т-грифа", id_creation_user=1, 
                        notice_workout_exercises="Техника: Встаньте в тренажер для тяги Т-грифа. Возьмитесь за рукояти, подтягивайте гриф к груди. Локти направлены вдоль тела. Сводите лопатки в верхней точке.",
                        id_muscle_category=17, gif_file_workout_exercises=None, vision_user=True),
        
        WorkoutExercises(id_workout_exercises=52, name_workout_exercises="Пуловер с гантелью лежа", id_creation_user=1, 
                        notice_workout_exercises="Техника: Лягте поперек скамьи, упираясь лопатками. Возьмите гантель двумя руками над грудью. Опускайте гантель за голову, чувствуя растяжение. Плавно возвращайте в исходное положение.",
                        id_muscle_category=17, gif_file_workout_exercises=None, vision_user=True),

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