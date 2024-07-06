from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STasksAdd

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("")
async def add_task(
        task: Annotated[STasksAdd, Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {"data": tasks}
