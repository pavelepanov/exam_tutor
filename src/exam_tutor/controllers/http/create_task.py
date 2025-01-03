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
    request_sound_files: list[UploadFile] | None = list[File(None)],
    request_file_files: list[UploadFile] | None = list[File(None)],
    request_photo_files: list[UploadFile] | None = list[File(None)],
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

    if request_sound_files is not None:
        request_sound_files_info = list()
        for file in request_sound_files:
            sound_bytes = await file.read()
            sound_file_type = file.content_type

            sound_info = {"payload": sound_bytes, "content_type": sound_file_type}

            request_sound_files_info.append(sound_info)
        request_files[FileType.SOUND] = request_sound_files_info

    else:
        sound_info = None
        request_files[FileType.SOUND] = sound_info

    if request_file_files is not None:
        request_file_files_info = list()
        for file in request_file_files:
            file_bytes = await file.read()
            file_file_type = file.content_type

            file_info = {
                "payload": file_bytes,
                "content_type": file_file_type,
            }

            request_file_files_info.append(file_info)

        request_files[FileType.FILE] = request_file_files_info

    else:
        file_info = None
        request_files[FileType.FILE] = file_info

    if request_photo_files is not None:
        request_photo_files_info = list()
        for file in request_photo_files:
            photo_bytes = await file.read()
            photo_file_type = file.content_type

            photo_info = {
                "payload": photo_bytes,
                "content_type": photo_file_type,
            }

            request_photo_files_info.append(photo_info)

        request_files[FileType.PHOTO] = request_photo_files_info

    return await interactor(request_data=request_data, request_files=request_files)
