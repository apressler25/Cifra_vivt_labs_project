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
    check_train_info:bool | int #если существует активная тренировка - id тренировки, если нет - false




class UserUpdate(BaseModel):
    name_user: Optional[str] = None
    info_restrictions_user: Optional[str] = None
    sub_user: Optional[bool] = None

class UserResponse(UserBase):
    date_registration_user: datetime
    
    model_config = ConfigDict(from_attributes=True)


##############
#домашняя страница
class Lasttrain(BaseModel):
    last_train_name_ex:str | None = None #Последняя тренировка список имен упражнений
    last_train_result_ex:str | None = None #Последняя тренировка список результатов упражнений



class HomeResponse(BaseModel):
    check_train_this_day:bool # проверка есть ли сегодня тренировка
    count_train_user:int | None = None #всего тренировок
    max_time_train:str | None = None #рекорд макс длительности тренировок в минутах
    name_examples_record_weight:str | None = None #имя упражнения с рекордом по весу
    max_weight_in_train:int | None = None#Вес рекорда упражнения 
    program_user_name_count:int | None = None#Имя программы пользователя
    last_train_ex:list[Lasttrain] # список с данными последней тренировки 






##############
#Упражнения 
#упражнение (вся информация)
class Workout_ex_item(BaseModel):
    name_workout_exercises: str #имя 
    id_creation_user: int #id пользователя создателя
    notice_workout_exercises: str | None = None #описание
    id_muscle_category: int  #категория мышц
    gif_file_workout_exercises: bytes | None = None #гифка

#Выборка упражнений созданных в список
class Workout_get_my_ex_item(Workout_ex_item):
    id_workout_exercises: int
    str_muscle_category: str

class Workout_my_ex(BaseModel):
    exercises:list[Workout_get_my_ex_item]

#создание
class Workout_create_ex(Workout_ex_item):
    pass
#вывод
class WorkoutExResponse(Workout_ex_item):
    id_workout_exercises: int

class Workout_ex_update(Workout_ex_item):
    name_workout_exercises: str | None = None
    id_creation_user: int | None = None
    notice_workout_exercises: str | None = None 
    id_muscle_category: int  | None = None
    gif_file_workout_exercises: bytes | None = None 
    class Config:
        from_attributes = True 


##############
#Программы Programs_workout

#Программа (вся инфа)


