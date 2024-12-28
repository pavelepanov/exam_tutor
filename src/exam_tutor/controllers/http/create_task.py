from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, status

from exam_tutor.application.interactors.create_task import (
    CreateTaskInteractor,
    CreateTaskRequest,
    CreateTaskResponse,
)

create_task_router = APIRouter()


@create_task_router.post("/", status_code=status.HTTP_201_CREATED)
@inject
async def create_task(
    interactor: FromDishka[CreateTaskInteractor],
    request_data: CreateTaskRequest,
) -> CreateTaskResponse:
    return await interactor(request_data)
