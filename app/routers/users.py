from fastapi import APIRouter, Depends, HTTPException, Response
from schemas.schemas_main import UserBase, UserCreate, UserResponse, ResponseUserAuthorize
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select
from sqlalchemy import delete 
from pydantic import TypeAdapter
from models.models_bd import User, TrainInfo, TrainPool, WorkoutExPool, ProgramsWorkout
from sqlalchemy.orm import selectinload
from fastapi.responses import RedirectResponse
from services.all_service import create_test_data

userrouter = APIRouter(prefix="/users", tags=["users"])



@userrouter.post("/", name=" добавить пользователя", response_model=UserResponse)
async def create_user(user:UserCreate, session:AsyncSession=Depends(get_async_session)):
    
    u = User()
    
    
    
    d=user.model_dump()
    for k in user.model_dump():
        setattr(u,k,d[k])
    session.add(u)
    await session.commit()
    await session.refresh(u)
    return UserResponse.model_validate(u)
    # raise HTTPException(status_code=404, detail='User not found')
    



@userrouter.get("/{telegram_id}", name="Вход в систему", response_model=ResponseUserAuthorize) #Проверяет входящего пользователя 
async def authorize_user(telegram_id:int, session: AsyncSession = Depends(get_async_session)):
    user = await session.scalar(select(User).where(User.id_telegram == telegram_id))
    if user is not None:
        query = (
        select(TrainInfo)
        .select_from(TrainInfo)
        .join(TrainPool, TrainInfo.id_train_info == TrainPool.id_train_info)
        .join(WorkoutExPool, TrainPool.id_ex_pool == WorkoutExPool.id_ex_pool)
        .join(ProgramsWorkout, WorkoutExPool.id_programs_workout == ProgramsWorkout.id_programs_workout)
        .join(User, ProgramsWorkout.id_user == User.id_user)
        .where(
            User.id_telegram == telegram_id,
            TrainInfo.check_train_info == True
            )
        )        
        train_user = await session.scalar(query)
        if train_user is not None:
            return ResponseUserAuthorize(was_registered=True, check_train_info=True)
        return ResponseUserAuthorize(was_registered=True, check_train_info=False)
    else:
        return ResponseUserAuthorize(was_registered=False, check_train_info=False)



################################# если пустые ячейки в БД ########################################
##################################################################################################
# @userrouter.post("/testdata", name=" создать тестовые данные") # если пустые ячейки
# async def create_testdat(session:AsyncSession=Depends(get_async_session)):
    
#     n = await create_test_data(session)
#     return {"message":n}
##################################################################################################