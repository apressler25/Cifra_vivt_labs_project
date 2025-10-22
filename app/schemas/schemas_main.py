from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime, date

class UserBase(BaseModel):
    id_telegram: int
    name_user: str
    info_restrictions_user: Optional[str] = None
    sub_user: bool

class UserCreate(BaseModel):
    id_telegram: int
    name_user: str
    pass

class ResponseUserAuthorize(BaseModel): #Возвращает, чтобы понять дальнейшие действия
    was_registered:bool #если уже был зарегистрирован - True, если нет - False и далее начало процесса настройки
    check_train_info:bool #если существует активная тренировка - True




class UserUpdate(BaseModel):
    name_user: Optional[str] = None
    info_restrictions_user: Optional[str] = None
    sub_user: Optional[bool] = None

class UserResponse(UserBase):
    id_user: int
    date_registration_user: datetime
    
    model_config = ConfigDict(from_attributes=True)
