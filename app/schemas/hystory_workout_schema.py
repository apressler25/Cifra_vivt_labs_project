from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date

# Схемы для истории тренировок

# 23. Запрос на получение дат тренировок за последние 3 месяца
class WorkoutDatesRequest(BaseModel):
    user_id: int

class WorkoutDatesResponse(BaseModel):
    dates: List[str]  # Список дат в формате "дд.мм.гг"

# 24. Запрос на получение всех тренировок
class AllWorkoutsRequest(BaseModel):
    user_id: int

class WorkoutSummary(BaseModel):
    workout_name: str #name_programs_workout из таблицы Train_info
    workout_id: int # id_train_info из таблицы Train_info
    date: str  # Дата в формате "20 июля" из datetime_start_train_info таблицы Train_info
    start_time: str  # Время начала в формате "HH:MM" из datetime_start_train_info таблицы Train_info
    end_time: str  # Время завершения в формате "HH:MM" из datetime_end_train_info таблицы Train_info
    has_progress: bool  # если у хотя бы у одного связанного элемента из таблицы Train_pool есть True в поле record_bool, ставится True, в ином случае - False 

class AllWorkoutsResponse(BaseModel):
    workouts: List[WorkoutSummary]

# 25. Запрос на получение детальной информации по тренировке
class WorkoutDetailRequest(BaseModel):
    workout_id: int

class WorkoutSet(BaseModel):
    set_number: int  # Номер подхода
    weight: float  # Рабочий вес
    repetitions: int  # Количество повторений
    has_progress: bool  # Был ли прогресс


class ExerciseResult(BaseModel):
    exercise_name: str  # Название упражнения
    target_muscle_group: str  # Целевая группа мышц
    sets: List[WorkoutSet]  # Список подходов
    average_rest: int  # Средний отдых в секундах

class WorkoutDetailResponse(BaseModel):
    workout_name: str  # Название тренировки
    workout_date: str  # Дата тренировки в формате "дд.мм.гг"
    workout_time: str  # Время тренировки в формате "18:30 - 19:37"
    duration: str  # Длительность тренировки (например, "1ч 7мин")
    volume: float  # Объем тренировки
    exercises: List[ExerciseResult]  # Список результатов по упражнениям

