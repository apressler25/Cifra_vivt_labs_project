from fastapi import APIRouter, Depends, HTTPException, Response
from schemas.user import UserSchema, UserList, UpdateUserSchema
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from db import User
from sqlalchemy.future import select
from sqlalchemy import delete 
from pydantic import TypeAdapter



userrouter = APIRouter(prefix="/users", tags=["users"])


@userrouter.get("/{user_id}", name="Пользователь", response_model=UserSchema)
async def get_user(user_id:int, session: AsyncSession = Depends(get_async_session)):
    # q = select(User).where(User.id == user_id)
    user = await session.get(User, user_id)
    if user is not None:
        return UserSchema.model_validate(user)
    raise HTTPException(status_code=404, detail='User not found')


@userrouter.delete('/{user_id}', name='Удалить пользователя', response_class=Response)
async def delete_user(user_id:int, session:AsyncSession=Depends(get_async_session)):
    q= delete(User).where(User.id == user_id)
    await session.execute(q)
    return Response(status_code=204)



@userrouter.post("/", name=" добавить пользователя", response_model=UserSchema)
async def create_user(user:UserSchema, session:AsyncSession=Depends(get_async_session)):
    u = User()
    d=user.model_dump()
    for k in user.model_dump():
        setattr(u,k,d[k])
    session.add(u)
    await session.commit()
    await session.refresh(u)
    return UserSchema.model_validate(u)
    # raise HTTPException(status_code=404, detail='User not found')




@userrouter.get("/", name="все пользователи", response_model=UserList)
async def get_all_user(session: AsyncSession=Depends(get_async_session)):
    q=select(User)
    users = (await session.execute(q)).scalars().all()
    if len(users)>0:
        user_adapter=TypeAdapter(list[UserSchema])
        return UserList(count=len(users), users=user_adapter.validate_python(users))
    else:
        raise HTTPException(status_code=404, detail='User not found')
    

@userrouter.put('/{user_id}', name='Обновить данные пользователя', response_model=UpdateUserSchema)
async def update_user(user_id:int, new_user_data:UpdateUserSchema, session: AsyncSession=Depends(get_async_session)):
    u = await session.get(User, user_id)
    if u is not None:
        data = new_user_data.model_dump()
        for key in data: 
            if data[key] is not None:
                setattr(u,key,data[key])
        session.add(u)
        await session.commit()
        await session.refresh(u)
        return UserSchema.model_validate(u)
    raise HTTPException(status_code=404, detail='UserSchema not found')