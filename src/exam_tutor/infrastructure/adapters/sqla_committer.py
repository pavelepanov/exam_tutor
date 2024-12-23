from sqlalchemy.ext.asyncio import AsyncSession

from exam_tutor.application.interfaces.committer import Committer


class CommitterImpl(Committer):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()
