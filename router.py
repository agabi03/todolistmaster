from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi import APIRouter

from repository import TaskRepository
from schemas import STaskADD, STask, STaskID

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post("")
async def add_task(
        task: Annotated[STaskADD, Depends()]
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return STaskID(id=task_id)


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks


@router.delete("")
async def delete_task(task_id: int) -> None:
    deleted = await TaskRepository.del_one(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
