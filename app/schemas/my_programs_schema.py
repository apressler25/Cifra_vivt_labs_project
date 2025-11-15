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
    workout_ex_in_program:list[workoutexSchema] | None = None 
    
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



class UserFeaturesResponseSchema(BaseModel):
    """Схема ответа получения особенностей пользователя"""
    features: str

class UpdateUserFeaturesSchema(BaseModel):
    """Схема для изменения особенностей пользователя"""
    features: str



class UpdateExerciseInWorkoutSchema(BaseModel):
    id_workout_exercises:int | None = None 
    max_target_iteration_ex_pool:int | None = None 
    min_target_iteration_ex_pool:int | None = None 
    approaches_target_ex_pool:int | None = None 
    weight_ex_pool:int | None = None 


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
