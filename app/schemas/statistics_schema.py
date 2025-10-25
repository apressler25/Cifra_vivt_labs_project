from pydantic import BaseModel, ConfigDict
from typing import Optional, List, Union
from datetime import datetime, date


class WorkoutStats(BaseModel):
    """Статистика тренировок"""
    total_workouts: int
    total_duration: int
    calories_burned: int
    average_workout_duration: float


class WeeklyStats(BaseModel):
    """Недельная статистика"""
    week_start: date
    week_end: date
    workouts_completed: int
    total_duration: int
    calories_burned: int
    streak_days: int


class MonthlyStats(BaseModel):
    """Месячная статистика"""
    month: str
    workouts_completed: int
    total_duration: int
    calories_burned: int
    favorite_exercise: str
    improvement_percentage: float


class UserRecord(BaseModel): #######################################################
    """Рекорд пользователя"""
    main_text: str
    description_text: str


class UserRecordsResponse(BaseModel): #######################################################
    """Ответ с рекордами пользователя"""
    
    records: List[UserRecord]



class WeeklyMuscleGroupsResponse(BaseModel): #######################################################
    """Ответ со списком целевых групп мышц за неделю"""
    muscle_ids: List[int]  # список id целевых групп мышц


class ExerciseSet(BaseModel):
    """Подход в упражнении"""
    weight: float
    reps: int
    date: date


class ExercisePoint(BaseModel):#######################################################
    """Статистика по упражнению"""
    weight:float
    num_iteration:int
    daate:str



class ExerciseStats(BaseModel):#######################################################
    """Статистика по упражнению"""
    exercise_name: str
    sets: List[ExercisePoint]  # [[вес, повторы, дата], ...]


class LastWorkoutsStatsResponse(BaseModel):#######################################################
    """Ответ со статистикой за последние 5 тренировок"""
    last_workout_stats: List[ExerciseStats]


class StatisticsResponse(BaseModel):
    """Ответ со статистикой"""
    success: bool = True
    data: dict
    message: Optional[str] = None
