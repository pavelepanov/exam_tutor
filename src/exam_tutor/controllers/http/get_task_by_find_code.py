from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends, status

from exam_tutor.application.interactors.get_task_by_find_code import (
    GetTaskByFindCodeRequest,
    GetTaskByFindCodeResponse,
)
from exam_tutor.entrypoint.ioc.interactors import GetTaskByFindCodeInteractor

get_task_by_find_code_router = APIRouter()


@get_task_by_find_code_router.get("/", status_code=status.HTTP_200_OK)
@inject
async def get_task_by_find_code(
    interactor: FromDishka[GetTaskByFindCodeInteractor],
    request_data: GetTaskByFindCodeRequest = Depends(),
) -> GetTaskByFindCodeResponse:
    return await interactor(request_data)
