from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.operators import eq

from exam_tutor.application.interfaces.task_data_gateway import TaskDataGateway
from exam_tutor.domain.entities.task import Task, TaskId
from exam_tutor.infrastructure.sqla_persistence.mappings.task import tasks_table


class SqlaTaskDataMapper(TaskDataGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def read_by_uuid(self, id: TaskId) -> Task | None:
        stmt = select(tasks_table).where(eq(tasks_table.id, id))

        task: Task | None = await self._session.execute(stmt).scalar_one_or_none()

        return task
