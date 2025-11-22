from fastapi import APIRouter, Depends
from schemas.user_schemas import ( UserCreateSchema, UserResponseSchema, ResponseUserAuthorizeSchema)
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select
from models.models_bd import (User, TrainInfo)
from services.all_service import delete_zero_iteration_approaches




userrouter = APIRouter(prefix="/users", tags=["ПОЛЬЗОВАТЕЛЬ"])


from datetime import datetime, timedelta

@userrouter.get("/{telegram_id}", name="Вход в систему", response_model=ResponseUserAuthorizeSchema)
async def authorize_user(telegram_id: int, session: AsyncSession = Depends(get_async_session)):
    # Определяем максимальное время от начала тренировки в часах
    MAX_TRAIN_DURATION_HOURS = 3  
    
    user = await session.scalar(select(User).where(User.id_telegram == telegram_id))
    
    if user is not None:
        query = (
            select(TrainInfo)
            .join(User, TrainInfo.Id_user == User.id_telegram)
            .where(
                User.id_telegram == telegram_id,
                TrainInfo.check_train_info == False,
                TrainInfo.datetime_end_train_info == None 
            )
        )        
        active_train = await session.scalar(query)
        
        # Если есть активная тренировка, проверяем ее длительность
        if active_train is not None:
            train_start_time = active_train.datetime_start_train_info
            current_time = datetime.now()
            train_duration = current_time - train_start_time
            
            # Если тренировка идет больше MAX_TRAIN_DURATION_HOURS часов
            if train_duration > timedelta(hours=MAX_TRAIN_DURATION_HOURS):
                # Завершаем тренировку
                active_train.datetime_end_train_info = current_time
                active_train.check_train_info = True
                
                # Выполняем очистку нулевых записей
                await delete_zero_iteration_approaches(telegram_id, session)
                
                # Сохраняем изменения
                await session.commit()
                
                return ResponseUserAuthorizeSchema(
                    was_registered=True, 
                    check_train_info=None,  # Тренировка завершена
                    sub_user=user.sub_user
                )
            else:
                # Тренировка активна и время в пределах нормы
                return ResponseUserAuthorizeSchema(
                    was_registered=True, 
                    check_train_info=active_train.id_train_info,
                    sub_user=user.sub_user
                )
        
        # Если активной тренировки нет
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
