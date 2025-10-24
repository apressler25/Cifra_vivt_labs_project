from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime, date

##############
#домашняя страница
class LasttrainSchema(BaseModel):
    last_train_name_ex:str | None = None #Последняя тренировка список имен упражнений
    last_train_result_ex:str | None = None #Последняя тренировка список результатов упражнений



class HomeResponseSchema(BaseModel):
    check_train_this_day:bool # проверка есть ли сегодня тренировка
    count_train_user:int | None = None #всего тренировок
    max_time_train:str | None = None #рекорд макс длительности тренировок в минутах
    record_train_info:list[LasttrainSchema] # список всех разновидностей упражнений выполненных пользователем с максимальным весом у них 
    program_user_name_count:int | None = None#Имя программы пользователя
    last_train_ex:list[LasttrainSchema] # список с данными последней тренировки 
