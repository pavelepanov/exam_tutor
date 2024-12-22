from typing import AsyncIterable

from dishka import AsyncContainer, Provider, Scope, make_async_container, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from exam_tutor.entrypoint.config import PostgresDsn


class SqlaProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_postgres_dsn(self) -> PostgresDsn:
        return PostgresDsn.from_env()

    @provide(scope=Scope.APP)
    def provide_engine(self, postgres_dsn: PostgresDsn) -> AsyncEngine:
        return create_async_engine(postgres_dsn.db_uri)

    @provide(scope=Scope.APP)
    def provide_sessionmaker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(
        self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session


def create_container() -> AsyncContainer:
    return make_async_container(
        SqlaProvider(),
    )
