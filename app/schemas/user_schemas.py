from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime, date

# class StatusResponse(BaseModel):
#     status: str  # "ok" или "fail"
#     message: str | None = None
#     data: dict | None = None #id если создание записи
    
class StatusResponse(BaseModel):
    status: bool  # "True" или "False"
    message: str | None = None
    data: dict | None = None


class UserBaseSchema(BaseModel):
    id_telegram: int
    name_user: str
    info_restrictions_user: Optional[str] = None
    sub_user: bool

class UserCreateSchema(BaseModel):
    id_telegram: int
    name_user: str
    pass

class ResponseUserAuthorizeSchema(BaseModel): #Возвращает, чтобы понять дальнейшие действия
    was_registered:bool #если уже был зарегистрирован - True, если нет - False и далее начало процесса настройки
    check_train_info:int | None = None#если существует активная тренировка - id тренировки, если нет - false
    sub_user:bool #есть или нет подписки




class UserUpdateSchema(BaseModel):
    name_user: Optional[str] = None
    info_restrictions_user: Optional[str] = None
    sub_user: Optional[bool] = None

class UserResponseSchema(UserBaseSchema):
    date_registration_user: datetime
    
    model_config = ConfigDict(from_attributes=True)