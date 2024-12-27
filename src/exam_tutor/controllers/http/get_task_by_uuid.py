

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, status, Query, Depends

from exam_tutor.application.interactors.get_task_by_find_code import (
    GetTaskByFindCodeResponse,
    GetTaskByFindCodeRequest,
)

from exam_tutor.entrypoint.ioc.interactors import GetTaskByUUIDInteractor


get_task_by_uuid_router = APIRouter()


@get_task_by_uuid_router.get("/", status_code=status.HTTP_200_OK)
@inject
async def get_task_by_uuid(
    interactor: FromDishka[GetTaskByUUIDInteractor], request_data: GetTaskByFindCodeRequest = Depends(),
) -> GetTaskByFindCodeResponse:
    return await interactor(request_data)
