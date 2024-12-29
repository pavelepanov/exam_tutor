from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends, File, UploadFile, status

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
    request_file: UploadFile = File(...),
    request_data: CreateTaskRequest = Depends(),
) -> CreateTaskResponse:
    request_file: bytes = await request_file.read()

    return await interactor(request_data=request_data, request_file=request_file)
