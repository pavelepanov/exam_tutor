import logging
from typing import AsyncIterable

from dishka import Provider, Scope, from_context, provide
from minio import Minio
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from exam_tutor.application.interfaces.committer import Committer
from exam_tutor.application.interfaces.file_manager import FileManager
from exam_tutor.application.interfaces.task_data_gateway import TaskDataGateway
from exam_tutor.domain.interfaces.generation_task_answer_video_link import (
    GenerationAnswerVideoLink,
)
from exam_tutor.domain.interfaces.generation_task_find_code import (
    GenerationTaskFindCode,
)
from exam_tutor.domain.interfaces.generation_task_id import GenerationTaskId
from exam_tutor.domain.services.task import TaskService
from exam_tutor.entrypoint.config import Config
from exam_tutor.infrastructure.adapters.generation_answer_video_link import (
    GenerationAnswerVideoLinkImpl,
)
from exam_tutor.infrastructure.adapters.generation_task_find_code import (
    GenerationTaskFindCodeImpl,
)
from exam_tutor.infrastructure.adapters.generation_task_id import GenerationTaskIdImpl
from exam_tutor.infrastructure.adapters.minio_manager import MinIOManager
from exam_tutor.infrastructure.adapters.sqla_committer import CommitterImpl
from exam_tutor.infrastructure.adapters.sqla_task_data_mapper import SqlaTaskDataMapper

logger = logging.getLogger(__name__)


class SqlaProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_engine(self, config: Config) -> AsyncEngine:
        return create_async_engine(config.postgres_config.db_uri)

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

    sqla_task_data_mapper = provide(
        SqlaTaskDataMapper, scope=Scope.REQUEST, provides=TaskDataGateway
    )
    sqla_committer = provide(CommitterImpl, scope=Scope.REQUEST, provides=Committer)


class TaskDomainProvider(Provider):
    task_service = provide(source=TaskService, scope=Scope.REQUEST)

    generation_task_find_code = provide(
        GenerationTaskFindCodeImpl, scope=Scope.REQUEST, provides=GenerationTaskFindCode
    )

    generation_task_id = provide(
        GenerationTaskIdImpl, scope=Scope.REQUEST, provides=GenerationTaskId
    )

    generation_task_answer_video_link = provide(
        GenerationAnswerVideoLinkImpl,
        scope=Scope.REQUEST,
        provides=GenerationAnswerVideoLink,
    )


class MinIOProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_minio_client(self, config: Config) -> Minio:
        logger.info("SECRET: %s", config.minio_config.secret_key)
        logger.info("ACCESS: %s", config.minio_config.access_key)
        client = Minio(
            endpoint=config.minio_config.uri,
            access_key=config.minio_config.access_key,
            secret_key=config.minio_config.secret_key,
            secure=config.minio_config.secure,
        )

        return client

    minio_manager = provide(MinIOManager, scope=Scope.REQUEST, provides=FileManager)


class ConfigProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)
