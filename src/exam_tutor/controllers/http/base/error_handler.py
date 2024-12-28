from functools import partial

from typing import cast

from starlette import status as code
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from exam_tutor.domain.error import Error
from exam_tutor.application.errors import DoesNotExistError


class HTTPError(Error): ...


async def validate(_: "Request", error: Exception, status: int) -> JSONResponse:
    error = cast(HTTPError, error)
    return JSONResponse(content={"message": error.message}, status_code=status)


def init_error_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        DoesNotExistError,
        partial(validate, status=code.HTTP_409_CONFLICT),
    )