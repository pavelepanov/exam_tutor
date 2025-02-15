from fastapi import APIRouter

from exam_tutor.controllers.http.create_task import create_task_router
from exam_tutor.controllers.http.get_task_by_find_code import (
    get_task_by_find_code_router,
)

tasks_router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

tasks_sub_routers = (
    get_task_by_find_code_router,
    create_task_router,
)

for router in tasks_sub_routers:
    tasks_router.include_router(router)
