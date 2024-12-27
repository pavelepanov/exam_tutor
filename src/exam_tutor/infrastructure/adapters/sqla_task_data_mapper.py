from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.operators import eq

from exam_tutor.application.interfaces.task_data_gateway import TaskDataGateway
from exam_tutor.domain.entities.task import Task, FindCode
from exam_tutor.infrastructure.sqla_persistence.mappings.task import tasks_table


class SqlaTaskDataMapper(TaskDataGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def read_by_find_code(self, find_code: FindCode) -> Task | None:
        stmt = select(Task).where(tasks_table.c.find_code == find_code)

        result = await self._session.execute(stmt)
        task: Task | None = result.scalars().one_or_none()

        return task
