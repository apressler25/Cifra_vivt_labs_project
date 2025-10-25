from fastapi import APIRouter, Depends
from schemas.user_schemas import ( UserCreateSchema, UserResponseSchema, ResponseUserAuthorizeSchema)
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select
from models.models_bd import (User, TrainInfo)





userrouter = APIRouter(prefix="/users", tags=["ПОЛЬЗОВАТЕЛЬ"])


@userrouter.get("/{telegram_id}", name="Вход в систему", response_model=ResponseUserAuthorizeSchema)
async def authorize_user(telegram_id: int, session: AsyncSession = Depends(get_async_session)):
    user = await session.scalar(select(User).where(User.id_telegram == telegram_id))
    if user is not None:
        query = (
            select(TrainInfo.id_train_info)
            .join(User, TrainInfo.Id_user == User.id_telegram)
            .where(
                User.id_telegram == telegram_id,
                TrainInfo.check_train_info == False
            )
        )        
        train_user = await session.scalar(query)
        if train_user is not None:
            return ResponseUserAuthorizeSchema(
                was_registered=True, 
                check_train_info=train_user,
                sub_user=user.sub_user
            )
        return ResponseUserAuthorizeSchema(
            was_registered=True, 
            check_train_info=None,
            sub_user=user.sub_user
        )
    else:
        return ResponseUserAuthorizeSchema(
            was_registered=False, 
            check_train_info=None,
            sub_user=False
        )



@userrouter.post("/createuser", name=" добавить пользователя", response_model=UserResponseSchema)
async def create_user(user:UserCreateSchema, session:AsyncSession=Depends(get_async_session)):
    u = User()
    d=user.model_dump()
    for k in user.model_dump():
        setattr(u,k,d[k])
    session.add(u)
    await session.commit()
    await session.refresh(u)
    return UserResponseSchema.model_validate(u)





















################################# если пустые ячейки в БД ########################################
##################################################################################################
from services.tests import create_test_data
@userrouter.post("/testdata", name=" создать тестовые данные") # если пустые ячейки
async def create_testdat(session:AsyncSession=Depends(get_async_session)):
    
    n = await create_test_data(session)
    return {"message":n}
##################################################################################################
