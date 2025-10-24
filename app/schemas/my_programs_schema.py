from pydantic import BaseModel, ConfigDict
from typing import Optional, List, Union
from datetime import datetime, date
##############
#Упражнения 
#упражнения пользователя (вся информация)
class WorkoutexitemSchema(BaseModel):
    name_workout_exercises: str #имя 
    id_creation_user: int #id пользователя создателя
    notice_workout_exercises: str | None = None #описание
    id_muscle_category: int  #категория мышц
    gif_file_workout_exercises: bytes | None = None #гифка

#Выборка упражнений созданных в список
class WorkoutgetmyexitemSchema(WorkoutexitemSchema):
    id_workout_exercises: int
    str_muscle_category: str

class WorkoutmyexSchema(BaseModel):
    exercises:list[WorkoutgetmyexitemSchema]

#создание
class WorkoutcreateexSchema(WorkoutexitemSchema):
    pass
#вывод
class WorkoutExResponseSchema(BaseModel):
    id_workout_exercises: int

class WorkoutexupdateSchema(BaseModel):
    name_workout_exercises: str | None = None
    notice_workout_exercises: str | None = None 
    id_muscle_category: int  | None = None
    gif_file_workout_exercises: bytes | None = None 
    vision_user: bool | None = None 
    class Config:
        from_attributes = True 





#Блок информации для визуализации "моей программы"
class workoutexSchema(BaseModel):
    id_workout_ex:int
    name_workout_ex:str
    max_target_iteration_ex_pool:int
    min_target_iteration_ex_pool:int
    approaches_target_ex_pool:int
    weight_ex_pool:int
    
    id_muscle_category:int
    name_muscle_category:str

class ProgramTrainSchema(BaseModel):
    id_program:int
    name_program:str
    day:str
    workout_ex_in_program:list[workoutexSchema]
    
class AllProgramsTrainSchema(BaseModel):
    program_train:list[ProgramTrainSchema]

#Обновление данных о тренировке
class UpdateProgramTrainSchema(BaseModel):
    name_programs_workout:str | None = None 
    week_day_programs_workout:str | None = None 


#Создание новой тренировки
class AddProgramTrainSchema(BaseModel):
    name_programs_workout:str
    week_day_programs_workout:str
    id_user:int
    



#Упражнения в рамках тренировки

class WorkoutExPoolItemSchema(BaseModel):
    id_ex_pool:int
    id_programs_workout:int
    id_workout_exercises:int
    max_target_iteration_ex_pool:int
    min_target_iteration_ex_pool:int
    approaches_target_ex_pool:int
    weight_ex_pool:int
    

class WorkoutExPoolItemCreateSchema(BaseModel):#добавление упражнения 
    id_programs_workout:int
    id_workout_exercises:int
    max_target_iteration_ex_pool:int
    min_target_iteration_ex_pool:int
    approaches_target_ex_pool:int
    weight_ex_pool:int



# Схемы для упражнений и программ тренировок согласно OpenAPI спецификации

class WorkoutcreateexSchema(BaseModel):
    """Схема для создания упражнения"""
    name_workout_exercises: str
    id_creation_user: int
    notice_workout_exercises: Optional[str] = None
    id_muscle_category: int
    gif_file_workout_exercises: Optional[Union[str, bytes]] = None

class WorkoutExResponseSchema(BaseModel):
    """Схема ответа создания упражнения"""
    name_workout_exercises: str
    id_creation_user: int
    notice_workout_exercises: Optional[str] = None
    id_muscle_category: int
    gif_file_workout_exercises: Optional[Union[str, bytes]] = None
    id_workout_exercises: int

class WorkoutexupdateSchema(BaseModel):
    """Схема для обновления упражнения"""
    name_workout_exercises: Optional[str] = None
    notice_workout_exercises: Optional[str] = None
    id_muscle_category: Optional[int] = None
    gif_file_workout_exercises: Optional[Union[str, bytes]] = None

class WorkoutgetmyexitemSchema(BaseModel):
    """Схема элемента упражнения пользователя"""
    name_workout_exercises: str
    id_creation_user: int
    notice_workout_exercises: Optional[str] = None
    id_muscle_category: int
    gif_file_workout_exercises: Optional[Union[str, bytes]] = None
    id_workout_exercises: int
    str_muscle_category: str

class WorkoutmyexSchema(BaseModel):
    """Схема списка упражнений пользователя"""
    exercises: List[WorkoutgetmyexitemSchema]

class workoutexSchema(BaseModel):
    """Схема упражнения в программе"""
    id_workout_ex: int
    name_workout_ex: str
    max_target_iteration_ex_pool: int
    min_target_iteration_ex_pool: int
    approaches_target_ex_pool: int
    weight_ex_pool: int
    id_muscle_category: int
    name_muscle_category: str

class ProgramTrainSchema(BaseModel):
    """Схема программы тренировки"""
    id_program: int
    name_program: str
    day: str
    workout_ex_in_program: List[workoutexSchema]

class AllProgramsTrainSchema(BaseModel):
    """Схема всех программ тренировок"""
    program_train: List[ProgramTrainSchema]

class UpdateProgramTrainSchema(BaseModel):
    """Схема обновления программы тренировки"""
    name_program: Optional[str] = None
    day: Optional[str] = None

class DeleteExerciseResponseSchema(BaseModel):
    """Схема ответа удаления упражнения"""
    status: str  # "ok" или "fail"

class UserFeaturesResponseSchema(BaseModel):
    """Схема ответа получения особенностей пользователя"""
    features: str

class UpdateUserFeaturesSchema(BaseModel):
    """Схема для изменения особенностей пользователя"""
    features: str

class UpdateUserFeaturesResponseSchema(BaseModel):
    """Схема ответа изменения особенностей пользователя"""
    status: str  # "ok" или "fail"

class AddExerciseToWorkoutSchema(BaseModel):
    """Схема для добавления упражнения в тренировку"""
    id_workout: int
    id_exercise: int
    min_reps: int  # минимальное количество повторений
    max_reps: int  # максимальное количество повторений
    approaches: int  # подходы
    working_weight: int  # рабочий вес

class AddExerciseToWorkoutResponseSchema(BaseModel):
    """Схема ответа добавления упражнения в тренировку"""
    status: str  # "ok" или "fail"

class RemoveExerciseFromWorkoutSchema(BaseModel):
    """Схема для удаления упражнения из тренировки"""
    id_exercise: int
    id_workout: int

class RemoveExerciseFromWorkoutResponseSchema(BaseModel):
    """Схема ответа удаления упражнения из тренировки"""
    status: str  # "ok" или "fail"

# class UpdateExerciseInWorkoutSchema(BaseModel):
#     """Схема для изменения упражнения в тренировке"""
#     id_workout: int | None = None 
#     id_exercise: int | None = None 
#     exercise_name: str | None = None  # название упражнения
#     min_reps: int  | None = None # минимальное количество повторений
#     max_reps: int | None = None  # максимальное количество повторений
#     approaches: int | None = None  # подходы
#     working_weight: int  | None = None # рабочий вес
    
class UpdateExerciseInWorkoutSchema(BaseModel):
    id_workout_exercises:int | None = None 
    max_target_iteration_ex_pool:int | None = None 
    min_target_iteration_ex_pool:int | None = None 
    approaches_target_ex_pool:int | None = None 
    weight_ex_pool:int | None = None 

class UpdateExerciseInWorkoutResponseSchema(BaseModel):
    """Схема ответа изменения упражнения в тренировке"""
    status: str  # "ok" или "fail"

class MuscleGroupSchema(BaseModel):
    """Схема группы мышц"""
    id_muscle_group: int
    name: str

class MuscleGroupsResponseSchema(BaseModel):
    """Схема ответа получения групп мышц"""
    muscle_groups: List[MuscleGroupSchema]

class ExerciseForSelectionSchema(BaseModel):
    """Схема упражнения для выбора"""
    id_exercise: int
    exercise_name: str
    description: Optional[str] = None
    gif_url: Optional[str] = None
    id_muscle_group: int
    not_recommended: bool

class ExercisesForSelectionResponseSchema(BaseModel):
    """Схема ответа получения упражнений для выбора"""
    exercises: List[ExerciseForSelectionSchema]

class CreateProgramTrainSchema(BaseModel):
    """Схема для добавления новой программы тренировок"""
    name_program: str
    day: str

class CreateProgramTrainResponseSchema(BaseModel):
    """Схема ответа добавления новой программы тренировок"""
    id_program: int

class DeleteProgramTrainSchema(BaseModel):
    """Схема для удаления программы тренировок"""
    id_program: int

class DeleteProgramTrainResponseSchema(BaseModel):
    """Схема ответа удаления программы тренировок"""
    status: str  # "ok" или "fail"
