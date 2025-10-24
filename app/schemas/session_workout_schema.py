from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime



# Базовые модели для подходов
class SetBase(BaseModel):
    """Базовые поля для подхода"""
    working_weight: float = Field(..., example=100.0)
    rest_start_time: Optional[datetime] = Field(None, example=datetime.now())
    rest_end_time: Optional[datetime] = Field(None, example=datetime.now())
    repetitions: int = Field(..., example=10)



class SetUpdate(SetBase):
    """Подход с ID для обновления (вход)"""
    set_id: int = Field(..., example=1)

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
    



# Модели для упражнений




class SetWithId(SetBase):
    """Подход с ID (для ответа)"""
    set_id: int = Field(..., example=1)

class ExerciseInWorkout(BaseModel):
    """Упражнение в процессе тренировки (для ответа получения упражнений)"""
    exercise_name: str = Field(..., example="Жим штанги лежа")
    exercise_history_id: int = Field(..., example=101)
    target_muscle_group_id: int = Field(..., example=1)
    target_muscle_group_name: str = Field(..., example="Грудь")
    description: str = Field(..., example="Базовое упражнение")
    completed_sets: List[SetWithId]

class GetWorkoutExercisesResponse(BaseModel):
    """Ответ на получение упражнений для ведения тренировки"""
    workout_name: str = Field(..., example="Силовая тренировка")
    exercises: List[ExerciseInWorkout]


class ExerciseHistoryUpdate(BaseModel):
    """Основные данные для обновления истории упражнения"""
    was_record: bool = Field(..., example=False)
    sets: List[SetUpdate]

# Запрос на создание тренировки
class CreateWorkoutRequest(BaseModel):
    """Входная схема для создания тренировки"""
    user_id: int

class CreateWorkoutResponse(BaseModel):
    """Ответ на создание тренировки"""
    workout_history_id: int

# Запрос на получение упражнений для ведения тренировки
class GetWorkoutExercisesRequest(BaseModel):
    """Входная схема для получения упражнений (хотя ID лучше передавать в URL)"""
    workout_history_id: int = Field(..., example=200)



# Запрос на обновление истории по упражнению
class UpdateExerciseHistoryRequest(ExerciseHistoryUpdate):
    """Входная схема для обновления истории по упражнению"""
    pass

# class UpdateExerciseHistoryResponse(BaseModel):
#     """Ответ на обновление истории по упражнению"""
#     status: StatusResponse = Field(..., example=StatusResponse.ok)

# Запрос на завершение тренировки
class CompleteWorkoutRequest(BaseModel):
    """Входная схема для завершения тренировки (хотя ID лучше передавать в URL)"""
    workout_history_id: int = Field(..., example=200)

# class CompleteWorkoutResponse(BaseModel):
#     """Ответ на завершение тренировки"""
#     status: StatusResponse = Field(..., example=StatusResponse.ok)