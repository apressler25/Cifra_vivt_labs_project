
from fastapi import APIRouter, Depends, HTTPException
from schemas.my_programs_schema import (WorkoutmyexSchema,  WorkoutcreateexSchema, WorkoutExResponseSchema, WorkoutgetmyexitemSchema, 
    WorkoutexupdateSchema, workoutexSchema, ProgramTrainSchema, AllProgramsTrainSchema, UpdateProgramTrainSchema, AddProgramTrainSchema, 
    WorkoutExPoolItemCreateSchema, UpdateExerciseInWorkoutSchema, 
    UserFeaturesResponseSchema, UpdateUserFeaturesSchema, MuscleGroupsResponseSchema, MuscleGroupSchema, ExerciseForSelectionSchema, ExercisesForSelectionResponseSchema)
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select

from models.models_bd import (User,  WorkoutExPool, ProgramsWorkout, 
                            WorkoutExercises,TargetMuscleCategory, Restrictions)



from schemas.user_schemas import StatusResponse



my_programs_router = APIRouter(prefix="/myprograms", tags=["МОИ ПРОГРАММЫ"])


#Получение списка всех созданных упражнений у конкретного пользователя
@my_programs_router.get('/Workoutex/{telegram_id}', summary="Получение списка созданных упражнений пользователем", response_model=WorkoutmyexSchema)
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
    
    return WorkoutmyexSchema(
        exercises=[
            WorkoutgetmyexitemSchema(
                
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
@my_programs_router.post("/createworkoutex/", summary=" добавить упражнение", response_model=WorkoutExResponseSchema)
async def create_workoutex(workoutex:WorkoutcreateexSchema, session:AsyncSession=Depends(get_async_session)):
    try:
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
        
        return StatusResponse(
            status=True,
            message="добавлено упражнение",
            data={
                "id_workout_exercises": u.id_workout_exercises
            }
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при создании программы: {str(e)}"
        )

@my_programs_router.delete("/deleteworkoutex/{workoutex_id}", response_model=StatusResponse, summary="Удалить упражнение")
async def delete_workout_exercise(
    workoutex_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    установка vision_user в False
    """
    try:
        # Находим упражнение
        exercise_query = select(WorkoutExercises).where(WorkoutExercises.id_workout_exercises == workoutex_id)
        exercise_result = await session.execute(exercise_query)
        exercise = exercise_result.scalar_one_or_none()
        
        if not exercise:
            return StatusResponse(
                status=False,
                message="Упражнение не найдено"
            )
        
        # Устанавливаем vision_user в False (мягкое удаление)
        exercise.vision_user = False
        
        session.add(exercise)
        await session.commit()
        await session.refresh(exercise)
        
        return StatusResponse(
            status=True,
            message="Упражнение успешно скрыто",
            data={
                "workoutex_id": workoutex_id,
            }
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при скрытии упражнения: {str(e)}"
        )


@my_programs_router.put('/updateworkoutex/{workoutex_id}', summary='Обновить данные упражнения', response_model=WorkoutExResponseSchema)
async def update_workoutex(workoutex_id:int, new_workoutex_data:WorkoutexupdateSchema, session: AsyncSession=Depends(get_async_session)):
    try:
        u = await session.get(WorkoutExercises, workoutex_id)
        if u is not None:
            # Явно обновляем каждое поле согласно схеме
            if new_workoutex_data.name_workout_exercises is not None:
                u.name_workout_exercises = new_workoutex_data.name_workout_exercises
                
            if new_workoutex_data.notice_workout_exercises is not None:
                u.notice_workout_exercises = new_workoutex_data.notice_workout_exercises
                
            if new_workoutex_data.id_muscle_category is not None:
                u.id_muscle_category = new_workoutex_data.id_muscle_category
                
            if new_workoutex_data.gif_file_workout_exercises is not None:
                u.gif_file_workout_exercises = new_workoutex_data.gif_file_workout_exercises
                
            if new_workoutex_data.vision_user is not None:
                u.vision_user = new_workoutex_data.vision_user
            
            session.add(u)
            await session.commit()
            await session.refresh(u)
            
            return StatusResponse(
                status=True,
                message="данные упражнения обновлены",
                data={
                    "id_workout_exercises": u.id_workout_exercises
                }
            )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при создании программы: {str(e)}"
        )

@my_programs_router.get("/programs/{telegram_id}", response_model=AllProgramsTrainSchema, summary="Получить программы тренировок пользователя")
async def get_user_programs(
    telegram_id: int, 
    session: AsyncSession = Depends(get_async_session)  # Правильная передача сессии
):
    """
    Получение всех программ тренировок пользователя с упражнениями
    """
    
    query = (
        select(
            ProgramsWorkout.id_programs_workout,
            ProgramsWorkout.name_programs_workout,
            ProgramsWorkout.week_day_programs_workout,
            WorkoutExPool.id_ex_pool,
            WorkoutExPool.max_target_iteration_ex_pool,
            WorkoutExPool.min_target_iteration_ex_pool,
            WorkoutExPool.approaches_target_ex_pool,
            WorkoutExPool.weight_ex_pool,
            WorkoutExercises.id_workout_exercises,
            WorkoutExercises.name_workout_exercises,
            TargetMuscleCategory.id_muscle_category,
            TargetMuscleCategory.name_muscle_category
        )
        .select_from(ProgramsWorkout)
        .join(WorkoutExPool, ProgramsWorkout.id_programs_workout == WorkoutExPool.id_programs_workout)
        .join(WorkoutExercises, WorkoutExPool.id_workout_exercises == WorkoutExercises.id_workout_exercises)
        .join(TargetMuscleCategory, WorkoutExercises.id_muscle_category == TargetMuscleCategory.id_muscle_category)
        .where(ProgramsWorkout.id_user == telegram_id)
        .order_by(
            ProgramsWorkout.id_programs_workout,
            WorkoutExPool.id_ex_pool
        )
    )
    
    result = await session.execute(query)
    programs_data = result.all()
    
    if not programs_data:
        raise HTTPException(status_code=404, detail="Программы тренировок не найдены")
    
    # Группируем данные по программам
    programs_dict = {}
    for row in programs_data:
        program_id = row[0]
        
        if program_id not in programs_dict:
            programs_dict[program_id] = {
                'id_program': program_id,
                'name_program': row[1],
                'day': row[2],
                'workout_ex_in_program': []
            }
        
        # Создаем объект упражнения
        exercise = workoutexSchema(
            id_workout_ex=row[8],  # WorkoutExercises.id_workout_exercises
            name_workout_ex=row[9],  # WorkoutExercises.name_workout_exercises
            max_target_iteration_ex_pool=row[4],  # WorkoutExPool.max_target_iteration_ex_pool
            min_target_iteration_ex_pool=row[5],  # WorkoutExPool.min_target_iteration_ex_pool
            approaches_target_ex_pool=row[6],  # WorkoutExPool.approaches_target_ex_pool
            weight_ex_pool=row[7],  # WorkoutExPool.weight_ex_pool
            id_muscle_category=row[10],  # TargetMuscleCategory.id_muscle_category
            name_muscle_category=row[11]  # TargetMuscleCategory.name_muscle_category
        )
        
        programs_dict[program_id]['workout_ex_in_program'].append(exercise)
    
    # Создаем список программ
    program_train_list = [
        ProgramTrainSchema(
            id_program=program_data['id_program'],
            name_program=program_data['name_program'],
            day=program_data['day'],
            workout_ex_in_program=program_data['workout_ex_in_program']
        )
        for program_data in programs_dict.values()
    ]
    
    # Возвращаем по схеме AllProgramsTrainSchema
    return AllProgramsTrainSchema(program_train=program_train_list)




#для обновления программы тренировки
@my_programs_router.put("/programs/{program_id}", response_model=UpdateProgramTrainSchema, summary="обновить программу тренировок")
async def update_program(program_id: int, update_data: UpdateProgramTrainSchema, session: AsyncSession = Depends(get_async_session)):
    try:
        u = await session.get(ProgramsWorkout, program_id)
        if u is not None:
            # Явно обновляем каждое поле
            if update_data.name_programs_workout is not None:
                u.name_programs_workout = update_data.name_programs_workout
                
            if update_data.week_day_programs_workout is not None:
                u.week_day_programs_workout = update_data.week_day_programs_workout
            
            session.add(u)
            await session.commit()
            await session.refresh(u)
            
            # return UpdateProgramTrainSchema(
            #     name_programs_workout=u.name_programs_workout,
            #     week_day_programs_workout=u.week_day_programs_workout
            # )
            return StatusResponse(
                        status=True,
                        message="данные тренировки обновлены",
                        data={
                            "id_programs_workout": u.id_programs_workout
                        }
                    )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при создании программы: {str(e)}"
        )




@my_programs_router.post("/programs/", response_model=StatusResponse, summary="Создать новую программу тренировок")
async def create_program(
    program_data: AddProgramTrainSchema,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Создание новой программы тренировки
    """
    try:
        # Проверяем существование пользователя
        user_query = select(User).where(User.id_telegram == program_data.id_user)
        user_result = await session.execute(user_query)
        user = user_result.scalar_one_or_none()
        
        if not user:
            return StatusResponse(
                status=False,
                message="Пользователь не найден"
            )
        
        # Создаем новую программу
        new_program = ProgramsWorkout(
            name_programs_workout=program_data.name_programs_workout,
            id_user=program_data.id_user,
            week_day_programs_workout=program_data.week_day_programs_workout
        )
        
        session.add(new_program)
        await session.commit()
        await session.refresh(new_program)
        
        return StatusResponse(
            status=True,
            message="Программа успешно создана",
            data={
                "program_id": new_program.id_programs_workout
            }
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при создании программы: {str(e)}"
        )

@my_programs_router.delete("/programs/{program_id}", response_model=StatusResponse, summary="Удалить программу тренировок")
async def delete_program(
    program_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        # Находим программу
        program_query = select(ProgramsWorkout).where(ProgramsWorkout.id_programs_workout == program_id)
        program_result = await session.execute(program_query)
        program = program_result.scalar_one_or_none()
        
        if not program:
            return StatusResponse(
                status=False,
                message="Программа тренировки не найдена"
            )
        
        # Удаляем программу
        await session.delete(program)
        await session.commit()
        
        return StatusResponse(
            status=True,
            message="Программа успешно удалена",
            data={"program_id": program_id}
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при удалении программы: {str(e)}"
        )
        
        






@my_programs_router.post("/addexercisetoworkout", response_model=StatusResponse, summary="Добавить упражнение в тренировку")
async def create_workout_ex_pool_item(
    workout_ex_data: WorkoutExPoolItemCreateSchema,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        # Проверяем существование программы тренировки
        program_query = select(ProgramsWorkout).where(ProgramsWorkout.id_programs_workout == workout_ex_data.id_programs_workout)
        program_result = await session.execute(program_query)
        program = program_result.scalar_one_or_none()
        
        if not program:
            return StatusResponse(
                status=False,
                message="Программа тренировки не найдена"
            )
        
        # Проверяем существование упражнения
        exercise_query = select(WorkoutExercises).where(WorkoutExercises.id_workout_exercises == workout_ex_data.id_workout_exercises)
        exercise_result = await session.execute(exercise_query)
        exercise = exercise_result.scalar_one_or_none()
        
        if not exercise:
            return StatusResponse(
                status=False,
                message="Упражнение не найдено"
            )
        
        # Создаем новую запись в пуле упражнений
        new_workout_ex_pool = WorkoutExPool(
            id_programs_workout=workout_ex_data.id_programs_workout,
            id_workout_exercises=workout_ex_data.id_workout_exercises,
            max_target_iteration_ex_pool=workout_ex_data.max_target_iteration_ex_pool,
            min_target_iteration_ex_pool=workout_ex_data.min_target_iteration_ex_pool,
            approaches_target_ex_pool=workout_ex_data.approaches_target_ex_pool,
            weight_ex_pool=workout_ex_data.weight_ex_pool
        )
        
        session.add(new_workout_ex_pool)
        await session.commit()
        await session.refresh(new_workout_ex_pool)
        
        return StatusResponse(
            status=True,
            message="Упражнение успешно добавлено в программу",
            data={
                "id_ex_pool": new_workout_ex_pool.id_ex_pool
            }
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при добавлении упражнения: {str(e)}"
        )
        
        

@my_programs_router.get("/userfeatures/{user_id}", response_model=UserFeaturesResponseSchema, summary="Получить особенности пользователя")
async def get_user_features(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        # Находим пользователя и получаем только info_restrictions_user
        user_query = select(User.info_restrictions_user).where(User.id_telegram == user_id)
        user_result = await session.execute(user_query)
        restrictions = user_result.scalar_one_or_none()
        
        if restrictions is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        # Если ограничений нет, возвращаем пустую строку
        features_text = restrictions if restrictions else "Ограничения не указаны"
        
        return UserFeaturesResponseSchema(features=features_text)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении особенностей пользователя: {str(e)}")
    

@my_programs_router.put("/userfeatures/{user_id}", response_model=StatusResponse, summary="Обновить особенности пользователя")
async def update_user_features(
    user_id: int,
    update_data: UpdateUserFeaturesSchema,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Обновление особенностей пользователя (ограничений)
    
    Args:
        user_id: ID пользователя (telegram_id)
        update_data: Новые ограничения пользователя
        
    Returns:
        Статус операции
    """
    try:
        # Находим пользователя
        user_query = select(User).where(User.id_telegram == user_id)
        user_result = await session.execute(user_query)
        user = user_result.scalar_one_or_none()
        
        if not user:
            return StatusResponse(
                status=False,
                message="Пользователь не найден"
            )
        
        # Обновляем поле info_restrictions_user
        if update_data.features is not None:
            user.info_restrictions_user = update_data.features
        
        session.add(user)
        await session.commit()
        
        return StatusResponse(
            status=True,
            message="Особенности пользователя успешно обновлены",
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при обновлении особенностей пользователя: {str(e)}"
        )
        
@my_programs_router.delete("/removeexercisefromworkout/{ex_pool_id}", response_model=StatusResponse, summary="Удалить упражнение из тренировки")
async def delete_workout_ex_pool_item(
    ex_pool_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Удаление упражнения из программы тренировки
    
    Args:
        ex_pool_id: ID записи в таблице WorkoutExPool
        
    Returns:
        Статус операции
    """
    try:
        # Находим запись в пуле упражнений
        ex_pool_query = select(WorkoutExPool).where(WorkoutExPool.id_ex_pool == ex_pool_id)
        ex_pool_result = await session.execute(ex_pool_query)
        ex_pool_item = ex_pool_result.scalar_one_or_none()
        
        if not ex_pool_item:
            return StatusResponse(
                status=False,
                message="Упражнение в тренировке не найдено"
            )
        
        # Сохраняем информацию для ответа
        deleted_data = {
            "id_ex_pool": ex_pool_item.id_ex_pool,
            "id_programs_workout": ex_pool_item.id_programs_workout,
            "id_workout_exercises": ex_pool_item.id_workout_exercises
        }
        
        # Удаляем запись из пула упражнений
        await session.delete(ex_pool_item)
        await session.commit()
        
        return StatusResponse(
            status=True,
            message="Упражнение успешно удалено из программы"
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при удалении упражнения: {str(e)}"
        )
        
@my_programs_router.put("/updateexerciseinworkout/{ex_pool_id}", response_model=StatusResponse, summary="Обновить данные упражнения в тренировке")
async def update_exercise_in_workout(
    ex_pool_id: int,
    update_data: UpdateExerciseInWorkoutSchema,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Обновление данных упражнения в программе тренировки
    
    Args:
        ex_pool_id: ID записи в таблице WorkoutExPool
        update_data: Новые данные упражнения
        
    Returns:
        Статус операции
    """
    try:
        # Находим запись в пуле упражнений
        ex_pool_query = select(WorkoutExPool).where(WorkoutExPool.id_ex_pool == ex_pool_id)
        ex_pool_result = await session.execute(ex_pool_query)
        ex_pool_item = ex_pool_result.scalar_one_or_none()
        
        if not ex_pool_item:
            return StatusResponse(
                status=False,
                message="Упражнение в тренировке не найдено"
            )
        
        # Проверяем существование нового упражнения, если указано
        if update_data.id_workout_exercises is not None:
            exercise_query = select(WorkoutExercises).where(WorkoutExercises.id_workout_exercises == update_data.id_workout_exercises)
            exercise_result = await session.execute(exercise_query)
            exercise = exercise_result.scalar_one_or_none()
            
            if not exercise:
                return StatusResponse(
                    status=False,
                    message="Указанное упражнение не найдено"
                )
        
        # Явно обновляем каждое поле
        if update_data.id_workout_exercises is not None:
            ex_pool_item.id_workout_exercises = update_data.id_workout_exercises
            
        if update_data.max_target_iteration_ex_pool is not None:
            ex_pool_item.max_target_iteration_ex_pool = update_data.max_target_iteration_ex_pool
            
        if update_data.min_target_iteration_ex_pool is not None:
            ex_pool_item.min_target_iteration_ex_pool = update_data.min_target_iteration_ex_pool
            
        if update_data.approaches_target_ex_pool is not None:
            ex_pool_item.approaches_target_ex_pool = update_data.approaches_target_ex_pool
            
        if update_data.weight_ex_pool is not None:
            ex_pool_item.weight_ex_pool = update_data.weight_ex_pool
        
        session.add(ex_pool_item)
        await session.commit()
        await session.refresh(ex_pool_item)
        
        return StatusResponse(
            status=True,
            message="Данные упражнения успешно обновлены"
        )
        
    except Exception as e:
        await session.rollback()
        return StatusResponse(
            status=False,
            message=f"Ошибка при обновлении данных упражнения: {str(e)}"
        )
        


@my_programs_router.get("/musclegroups/", response_model=MuscleGroupsResponseSchema, summary="Получить список групп мышц")
async def get_muscle_groups(
    session: AsyncSession = Depends(get_async_session)
):
    try:
        # Получаем все категории мышц с сортировкой по ID
        muscle_groups_query = select(TargetMuscleCategory).order_by(TargetMuscleCategory.id_muscle_category)
        muscle_groups_result = await session.execute(muscle_groups_query)
        muscle_groups = muscle_groups_result.scalars().all()
        
        muscle_groups_list = [
            MuscleGroupSchema(
                id_muscle_group=group.id_muscle_category,
                name=group.name_muscle_category
            )
            for group in muscle_groups
        ]
        
        return MuscleGroupsResponseSchema(muscle_groups=muscle_groups_list)
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Ошибка при получении списка групп мышц: {str(e)}"
        )
        

@my_programs_router.get("/exercisesforselection/{muscle_group_id}/{user_id}", response_model=ExercisesForSelectionResponseSchema, summary="Получить упражнения для выбора по группе мышц")
async def get_exercises_for_selection(
    muscle_group_id: int, 
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Получение упражнений для выбора по группе мышц
    
    Args:
        muscle_group_id: ID группы мышц
        user_id: ID пользователя (telegram_id)
        
    Returns:
        Список упражнений с информацией о рекомендациях
    """
    try:
        # Получаем упражнения, созданные пользователем или системой (id_creation_user = 1)
        exercises_query = (
            select(
                WorkoutExercises.id_workout_exercises,
                WorkoutExercises.name_workout_exercises,
                WorkoutExercises.notice_workout_exercises,
                WorkoutExercises.gif_file_workout_exercises,
                WorkoutExercises.id_muscle_category,
                WorkoutExercises.vision_user
            )
            .where(
                WorkoutExercises.id_muscle_category == muscle_group_id,
                WorkoutExercises.vision_user == True,  # Только видимые упражнения
                WorkoutExercises.id_creation_user.in_([user_id, 1])  # Упражнения пользователя или системные
            )
        )
        
        exercises_result = await session.execute(exercises_query)
        exercises = exercises_result.all()
        
        # Получаем ограничения пользователя для определения not_recommended
        restrictions_query = (
            select(Restrictions.id_workout_exercises)
            .where(Restrictions.id_user == user_id)
        )
        restrictions_result = await session.execute(restrictions_query)
        restricted_exercise_ids = {row[0] for row in restrictions_result.all()}
        
        # Формируем список упражнений
        exercises_list = []
        for ex in exercises:
            exercise_id = ex[0]
            # Определяем, не рекомендуется ли упражнение (есть в ограничениях)
            not_recommended = exercise_id in restricted_exercise_ids
            
            exercises_list.append(
                ExerciseForSelectionSchema(
                    id_exercise=exercise_id,
                    exercise_name=ex[1],  # name_workout_exercises
                    description=ex[2],    # notice_workout_exercises
                    gif_url=ex[3],        # gif_file_workout_exercises 
                    id_muscle_group=ex[4],  # id_muscle_category
                    not_recommended=not_recommended
                )
            )
        
        return ExercisesForSelectionResponseSchema(exercises=exercises_list)
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Ошибка при получении упражнений: {str(e)}"
        )





