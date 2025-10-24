
from fastapi import APIRouter, Depends, HTTPException, Response
from schemas.statistics_schema import UserRecord, UserRecordsResponse, WeeklyMuscleGroupsResponse, LastWorkoutsStatsResponse, ExerciseStats
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select
from sqlalchemy import delete 
from pydantic import TypeAdapter
from models.models_bd import (User, TrainInfo, TrainPool, WorkoutExPool, ProgramsWorkout, 
                            WorkoutExercises,TargetMuscleCategory,ApproachesRec, Restrictions)
from sqlalchemy.orm import selectinload
from fastapi.responses import RedirectResponse
from sqlalchemy import func, extract, and_, or_
from datetime import datetime, date, timedelta
from schemas.user_schemas import StatusResponse


statistics_router = APIRouter(prefix="/statistics", tags=["СТАТИСТИКА"])

# @statistics_router.get('/records/{user_id}', summary="Получение рекордов пользователя", response_model=UserRecordsResponse)
# async def get_workoutex(user_id:int, session: AsyncSession = Depends(get_async_session)):
    
# class UserRecordsResponse(BaseModel):
#     """Ответ с рекордами пользователя"""
#     success: bool = True
#     data: List[UserRecord]
#     message: Optional[str] = None
    
# class UserRecord(BaseModel):
#     """Рекорд пользователя"""
#     main_text: str
#     description_text: str

#ПРОБЛЕМКА ПРОПУСК РЕКОРДОВ

