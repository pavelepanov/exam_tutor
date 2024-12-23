from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from exam_tutor.controllers.http.task.task_router import tasks_router

root_router = APIRouter()


@root_router.get("/", tags=["General"])
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="docs/")


root_sub_routers = (tasks_router,)

for router in root_sub_routers:
    root_router.include_router(router)
