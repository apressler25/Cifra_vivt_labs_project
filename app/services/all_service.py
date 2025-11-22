
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from sqlalchemy.future import select
from models.models_bd import (TrainInfo, ApproachesRec,TrainPool)
from sqlalchemy import delete, exists



async def delete_zero_iteration_approaches(id_telegram: int, session: AsyncSession):

    try:
        # Шаг 1: Находим и удаляем подходы с нулевыми итерациями, собирая информацию о родителях
        stmt_approaches_info = (
            select(
                ApproachesRec.id_approaches_rec,
                ApproachesRec.id_train_pool,
                TrainPool.id_train_info
            )
            .join(TrainPool)
            .join(TrainInfo)
            .where(
                TrainInfo.Id_user == id_telegram,
                ApproachesRec.num_iteration_approaches_rec == 0
            )
        )
        
        result_approaches_info = await session.execute(stmt_approaches_info)
        approaches_data = result_approaches_info.all()
        
        if not approaches_data:
            return

        approach_ids = [data.id_approaches_rec for data in approaches_data]
        train_pool_ids = list(set(data.id_train_pool for data in approaches_data))
        train_info_ids = list(set(data.id_train_info for data in approaches_data))

        delete_approaches_stmt = (
            delete(ApproachesRec)
            .where(ApproachesRec.id_approaches_rec.in_(approach_ids))
        )
        await session.execute(delete_approaches_stmt)
        
        # Шаг 2: Находим Train_pool без подходов
        stmt_empty_train_pools = (
            select(TrainPool.id_train_pool)
            .where(
                TrainPool.id_train_pool.in_(train_pool_ids),
                ~exists().where(ApproachesRec.id_train_pool == TrainPool.id_train_pool)
            )
        )
        result_empty_pools = await session.execute(stmt_empty_train_pools)
        empty_train_pool_ids = [row[0] for row in result_empty_pools.all()]

        if empty_train_pool_ids:
            delete_train_pools_stmt = (
                delete(TrainPool)
                .where(TrainPool.id_train_pool.in_(empty_train_pool_ids))
            )
            await session.execute(delete_train_pools_stmt)
        
        # Шаг 3: Находим Train_info без Train_pool
        stmt_empty_train_info = (
            select(TrainInfo.id_train_info)
            .where(
                TrainInfo.id_train_info.in_(train_info_ids),
                ~exists().where(TrainPool.id_train_info == TrainInfo.id_train_info)
            )
        )
        result_empty_info = await session.execute(stmt_empty_train_info)
        empty_train_info_ids = [row[0] for row in result_empty_info.all()]

        if empty_train_info_ids:
            delete_train_info_stmt = (
                delete(TrainInfo)
                .where(TrainInfo.id_train_info.in_(empty_train_info_ids))
            )
            await session.execute(delete_train_info_stmt)
        
        await session.commit()
        
    except Exception as e:
        await session.rollback()
        raise e