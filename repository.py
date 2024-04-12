from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import STaskADD, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskADD) -> int:
        async with new_session() as session:
            task_dict = data.dict()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.from_orm(task_model) for task_model in task_models]
            return task_schemas

    @classmethod
    async def del_one(cls, task_id: int) -> bool:
        async with new_session() as session:
            query = select(TaskOrm).where(TaskOrm.id == task_id)
            result = await session.execute(query)
            task_to_delete = result.scalars().first()
            if task_to_delete:
                await session.delete(task_to_delete)
                await session.commit()
                return True
            return False

