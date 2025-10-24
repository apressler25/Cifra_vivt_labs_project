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


class UserRecord(BaseModel):
    """Рекорд пользователя"""
    main_text: str
    description_text: str


class UserRecordsResponse(BaseModel):
    """Ответ с рекордами пользователя"""
    success: bool = True
    data: List[UserRecord]
    message: Optional[str] = None


class WeeklyMuscleGroupsResponse(BaseModel):
    """Ответ со списком целевых групп мышц за неделю"""
    success: bool = True
    data: List[int]  # список id целевых групп мышц
    message: Optional[str] = None


class ExerciseSet(BaseModel):
    """Подход в упражнении"""
    weight: float
    reps: int
    date: date


class ExerciseStats(BaseModel):
    """Статистика по упражнению"""
    exercise_name: str
    sets: List[List[float | int | str]]  # [[вес, повторы, дата], ...]


class LastWorkoutsStatsResponse(BaseModel):
    """Ответ со статистикой за последние 5 тренировок"""
    success: bool = True
    data: List[ExerciseStats]
    message: Optional[str] = None


class StatisticsResponse(BaseModel):
    """Ответ со статистикой"""
    success: bool = True
    data: dict
    message: Optional[str] = None
