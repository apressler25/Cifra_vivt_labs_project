from fastapi import APIRouter, Depends, HTTPException, Response
from schemas.schemas_main import (UserBase, UserCreate, UserResponse, ResponseUserAuthorize, 
    Workout_my_ex, Workout_ex_item, Workout_create_ex, WorkoutExResponse, Workout_get_my_ex_item, 
    Workout_ex_update, HomeResponse,Lasttrain)
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select
from sqlalchemy import delete 
from pydantic import TypeAdapter
from models.models_bd import (User, TrainInfo, TrainPool, WorkoutExPool, ProgramsWorkout, 
                            WorkoutExercises,TargetMuscleCategory,ApproachesRec)
from sqlalchemy.orm import selectinload
from fastapi.responses import RedirectResponse
from sqlalchemy import func, extract, and_, or_
from datetime import datetime, date, timedelta

userrouter = APIRouter(prefix="/users", tags=["users"])


@userrouter.get("/{telegram_id}", name="Вход в систему", response_model=ResponseUserAuthorize) #Проверяет входящего пользователя 
async def authorize_user(telegram_id:int, session: AsyncSession = Depends(get_async_session)):
    user = await session.scalar(select(User).where(User.id_telegram == telegram_id))
    if user is not None:
        query = (
        select(TrainInfo.id_train_info)
        # .select_from(TrainInfo)
        .join(User, TrainInfo.Id_user == User.id_telegram)
        .where(
            User.id_telegram == telegram_id,
            TrainInfo.check_train_info == True
            )
        )        
        train_user = await session.scalar(query)
        if train_user is not None:
            return ResponseUserAuthorize(was_registered=True, check_train_info=train_user)
        return ResponseUserAuthorize(was_registered=True, check_train_info=False)
    else:
        return ResponseUserAuthorize(was_registered=False, check_train_info=False)



@userrouter.post("/createuser", name=" добавить пользователя", response_model=UserResponse)
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
    





#Получение списка всех созданных упражнений у конкретного пользователя
@userrouter.get('/Workoutex/{telegram_id}', name="Получение списка созданных упражнений пользователем", response_model=Workout_my_ex)
async def get_workoutex(telegram_id:int, session: AsyncSession = Depends(get_async_session)):
    q = (
        select(
            WorkoutExercises.id_workout_exercises.label('id_ex'),
            WorkoutExercises.name_workout_exercises.label('name_ex'),
            WorkoutExercises.id_creation_user.label('id_user_create'),
            WorkoutExercises.notice_workout_exercises.label('notice_ex'),
            TargetMuscleCategory.id_muscle_category.label('id_muscle_category'),
            TargetMuscleCategory.name_muscle_category.label('muscle_category')
        )
        .join(TargetMuscleCategory, WorkoutExercises.id_muscle_category == TargetMuscleCategory.id_muscle_category)
        .join(User, WorkoutExercises.id_creation_user == User.id_telegram)
        .where(User.id_telegram == telegram_id)
        )
    
    result = await session.execute(q)
    exercises = result.all()
    
    return Workout_my_ex(
        exercises=[
            Workout_get_my_ex_item(
                
                id_workout_exercises=ex.id_ex,
                name_workout_exercises=ex.name_ex,
                id_creation_user=ex.id_user_create,
                notice_workout_exercises=ex.notice_ex,
                id_muscle_category=ex.id_muscle_category,
                str_muscle_category=ex.muscle_category
            ) for ex in exercises
        ]
    )



# Создание упражнения пользователем
@userrouter.post("/createworkoutex/", name=" добавить упражнение", response_model=WorkoutExResponse)
async def create_workoutex(workoutex:Workout_create_ex, session:AsyncSession=Depends(get_async_session)):
    u = WorkoutExercises(
        name_workout_exercises=workoutex.name_workout_exercises,
        id_creation_user=workoutex.id_creation_user,
        notice_workout_exercises=workoutex.notice_workout_exercises,
        id_muscle_category=workoutex.id_muscle_category,
        gif_file_workout_exercises=workoutex.gif_file_workout_exercises
    )
    session.add(u)
    await session.commit()
    await session.refresh(u)
    
    return WorkoutExResponse(
        id_workout_exercises=u.id_workout_exercises,
        name_workout_exercises=u.name_workout_exercises,
        id_creation_user=u.id_creation_user,
        notice_workout_exercises=u.notice_workout_exercises,
        id_muscle_category=u.id_muscle_category,
        gif_file_workout_exercises=u.gif_file_workout_exercises
    )

@userrouter.put('/updateworkoutex/{workoutex_id}', name='Обновить данные упражнения', response_model=Workout_ex_update)
async def update_workoutex(workoutex_id:int, new_workoutex_data:Workout_ex_update, session: AsyncSession=Depends(get_async_session)):
    u = await session.get(WorkoutExercises, workoutex_id)
    if u is not None:
        data = new_workoutex_data.model_dump()
        for key in data:
            if data[key] is not None:
                setattr(u,key,data[key])
        session.add(u)
        await session.commit()
        await session.refresh(u)
        return WorkoutExResponse(
        id_workout_exercises=u.id_workout_exercises,
        name_workout_exercises=u.name_workout_exercises,
        id_creation_user=u.id_creation_user,
        notice_workout_exercises=u.notice_workout_exercises,
        id_muscle_category=u.id_muscle_category,
        gif_file_workout_exercises=u.gif_file_workout_exercises)




#Получение всех программ тренировок А Б В ... пользователя с вложенностями (упражнениями)


#Создание тренировки







@userrouter.get("/main/{telegram_id}", name="Домашняя страница", response_model=HomeResponse)
async def get_mainpage(telegram_id:int, session: AsyncSession = Depends(get_async_session)):
    today = date.today()
    
    
    # 1. Проверка есть ли сегодня тренировка
    russian_days = {
    0: 'Понедельник',  # Monday
    1: 'Вторник',      # Tuesday
    2: 'Среда',        # Wednesday
    3: 'Четверг',      # Thursday
    4: 'Пятница',      # Friday
    5: 'Суббота',      # Saturday
    6: 'Воскресенье'   # Sunday
}
    today_russian = russian_days[today.weekday()]
    today_train_query = (
        select(func.count(ProgramsWorkout.id_programs_workout))
        .where(
            ProgramsWorkout.id_user == telegram_id,
            ProgramsWorkout.week_day_programs_workout == today_russian  # Название дня недели
        )
    )
    today_train_count = await session.scalar(today_train_query)
    check_train_this_day = today_train_count > 0


    # 2. Всего тренировок пользователя
    count_train_query = (
        select(func.count(TrainInfo.id_train_info))
        .where(TrainInfo.Id_user == telegram_id)
    )
    count_train_user = await session.scalar(count_train_query) or 0

    # 3. Общее время всех тренировок в формате "1 ч 30 мин"
    total_time_query = (
        select(
            func.sum(
                extract('epoch', TrainInfo.datetime_end_train_info - TrainInfo.datetime_start_train_info)
            )
        )
        .where(
            TrainInfo.Id_user == telegram_id,
            TrainInfo.datetime_end_train_info.isnot(None)
        )
    )
    total_seconds = await session.scalar(total_time_query) or 0

    # Конвертируем секунды в часы и минуты
    if total_seconds > 0:
        total_minutes = int(total_seconds // 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        max_time_train = f"{hours} ч {minutes} мин"
    else:
        max_time_train = "0 ч 0 мин"




    # 4. Упражнение с рекордом по весу и сам вес
    max_weight_query = (
        select(
            WorkoutExercises.name_workout_exercises,
            ApproachesRec.weight_approaches_rec
        )
        .join(TrainPool, ApproachesRec.id_train_pool == TrainPool.id_train_pool)
        .join(WorkoutExercises, TrainPool.id_workout_exercises == WorkoutExercises.id_workout_exercises)
        .join(TrainInfo, TrainPool.id_train_info == TrainInfo.id_train_info)
        .where(TrainInfo.Id_user == telegram_id)
        .order_by(ApproachesRec.weight_approaches_rec.desc())
        .limit(1)
    )
    max_weight_result = await session.execute(max_weight_query)
    max_weight_data = max_weight_result.first()
    
    name_examples_record_weight = max_weight_data[0] if max_weight_data else None
    max_weight_in_train = max_weight_data[1] if max_weight_data else 0

    # 5. Количество программ пользователя
    program_count_query = (
        select(func.count(ProgramsWorkout.id_programs_workout))
        .where(ProgramsWorkout.id_user == telegram_id)
    )
    program_user_name_count = await session.scalar(program_count_query) or 0

    # 6. Данные последней тренировки
    last_train_query = (
        select(
            TrainInfo.id_train_info,
            TrainInfo.datetime_start_train_info
        )
        .where(TrainInfo.Id_user == telegram_id)
        .order_by(TrainInfo.datetime_start_train_info.desc())
        .limit(1)
    )
    last_train_info = await session.execute(last_train_query)
    last_train_data = last_train_info.first()

    last_train_exercises = []
    if last_train_data:
        last_train_id = last_train_data[0]
        
        # Получаем упражнения из последней тренировки с группировкой по упражнениям
        last_exercises_query = (
            select(
                WorkoutExercises.name_workout_exercises,
                func.max(ApproachesRec.weight_approaches_rec).label('max_weight'),
                func.max(ApproachesRec.num_iteration_approaches_rec).label('max_iterations')
            )
            .select_from(TrainPool)
            .join(WorkoutExercises, TrainPool.id_workout_exercises == WorkoutExercises.id_workout_exercises)
            .join(ApproachesRec, TrainPool.id_train_pool == ApproachesRec.id_train_pool)
            .where(TrainPool.id_train_info == last_train_id)
            .group_by(WorkoutExercises.name_workout_exercises)  # Группируем по названию упражнения
        )
        last_exercises_result = await session.execute(last_exercises_query)
        last_exercises = last_exercises_result.all()
        
        for ex in last_exercises:
            exercise_name = ex[0]
            max_weight = ex[1]
            max_iterations = ex[2]
            result_str = f"{max_weight}кг × {max_iterations}повт."
            
            last_train_exercises.append(
                Lasttrain(
                    last_train_name_ex=exercise_name,
                    last_train_result_ex=result_str
                )
            )

        return HomeResponse(
            check_train_this_day=check_train_this_day,
            count_train_user=count_train_user,
            max_time_train=max_time_train,
            name_examples_record_weight=name_examples_record_weight,
            max_weight_in_train=max_weight_in_train,
            program_user_name_count=program_user_name_count,
            last_train_ex=last_train_exercises
        )
    
    
    # return HomeResponse(
    #     check_train_this_day=# проверка есть ли сегодня тренировка
        

    #     count_train_user=#всего тренировок
    #     max_time_train= #рекорд макс длительности тренировок в минутах
    #     name_examples_record_weight= #имя упражнения с рекордом по весу
    #     max_weight_in_train=#Вес рекорда упражнения 
    #     program_user_name_count=#Имя программы пользователя
        
        
    #     last_train_ex=[# список с данными последней тренировки 
    #         Lasttrain(
    #             last_train_name_ex=ex.id_ex,
    #             nlast_train_result_ex=ex.name_ex,
    #         ) for ex in exercises
    #     ]
    # )















################################# если пустые ячейки в БД ########################################
##################################################################################################
from services.tests import create_test_data
@userrouter.post("/testdata", name=" создать тестовые данные") # если пустые ячейки
async def create_testdat(session:AsyncSession=Depends(get_async_session)):
    
    n = await create_test_data(session)
    return {"message":n}
##################################################################################################