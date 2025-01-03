from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends, File, UploadFile, status

from exam_tutor.application.enums import FileType
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
    request_answer_video_file: UploadFile | None = File(None),
    request_data: CreateTaskRequest = Depends(),
) -> CreateTaskResponse:
    request_files = dict()

    if request_answer_video_file is not None:
        request_answer_video_file_bytes: bytes = await request_answer_video_file.read()

        answer_video_info = {
            "payload": request_answer_video_file_bytes,
            "content_type": request_answer_video_file.content_type,
        }

        request_files[FileType.ANSWER_VIDEO] = answer_video_info

    else:
        answer_video_info = None
        request_files[FileType.ANSWER_VIDEO] = answer_video_info

    return await interactor(request_data=request_data, request_files=request_files)
