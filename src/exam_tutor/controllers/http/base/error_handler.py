from functools import partial
from typing import cast

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status as code

from exam_tutor.application.errors import DoesNotExistError
from exam_tutor.domain.error import Error


class HTTPError(Error): ...


async def validate(_: Request, error: Exception, status: int) -> JSONResponse:
    error = cast(HTTPError, error)
    return JSONResponse(content={"message": error.message}, status_code=status)


def init_error_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        DoesNotExistError,
        partial(validate, status=code.HTTP_409_CONFLICT),
    )
