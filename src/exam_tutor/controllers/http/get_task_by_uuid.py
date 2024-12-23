from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, status

from exam_tutor.application.interactors.get_task_by_uuid import (
    GetTaskByUUIDRequest,
    GetTaskByUUIDResponse,
)

get_task_by_uuid_router = APIRouter()


@get_task_by_uuid_router.get("/{id}", status_code=status.HTTP_200_OK)
@inject
async def get_task_by_uuid(
    request_data: GetTaskByUUIDRequest, intercator: FromDishka[get_task_by_uuid_router]
) -> GetTaskByUUIDResponse:
    return await intercator(request_data)
