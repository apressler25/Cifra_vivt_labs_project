from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime



# Базовые модели для подходов
class Approaches(BaseModel):
    id_approaches_rec:int
    weight_approaches_rec:int
    rest_time_up_approaches_rec:datetime
    rest_time_down_approaches_rec:datetime
    num_iteration_approaches_rec:int


class TakeInfoTrainPool(BaseModel):
    id_train_pool:int
    approaches_rec:list[Approaches]


class TakeInfoTrainInfo(BaseModel):
    id_train_info:int
    datetime_start_train_info:datetime
    name_program_workout:str
    examples_train:list[TakeInfoTrainPool]

class ApproachesWithExercise(BaseModel):
    working_weight: int
    rest_start_time: datetime | None = None
    rest_end_time: datetime | None = None
    repetitions: int
    set_id: int

class TakeInfoTrainPoolWithExercise(BaseModel):
    exercise_name: str
    exercise_history_id: int
    target_muscle_group_id:int
    target_muscle_group_name:str
    description:str
    completed_sets: list[ApproachesWithExercise]
    

class TakeInfoTrainInfoWithExercises(BaseModel):
    workout_name: str
    exercises: list[TakeInfoTrainPoolWithExercise]


class ApproachesWithExerciseUpdate(BaseModel):
    
    working_weight: int | None = None # weight_approaches_rec в таблице Approaches_rec
    rest_start_time: datetime | None = None #  rest_time_up_approaches_rec  в таблице Approaches_rec
    rest_end_time: datetime | None = None  #rest_time_down_approaches_rec в таблицеApproaches_rec
    repetitions: int | None = None   #num_iteration_approaches_rec в таблице Approaches_rec
    set_id: int   #НЕ ИЗМЕНЯЕТСЯ, ИСПОЛЬЗУЕТСЯ ДЛЯ УКАЗАНИЯ id в таблице Approaches_rec
    was_record:bool | None = None   #record_bool в таблице Approaches_rec

class TakeInfoTrainPoolWithExerciseUpdate(BaseModel):

    completed_sets: list[ApproachesWithExerciseUpdate]
    was_record:bool | None = None # record_bool в таблице Train_pool
    

# Запрос на создание тренировки
class CreateWorkoutRequest(BaseModel):
    user_id: int
