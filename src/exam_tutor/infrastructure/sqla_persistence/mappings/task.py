from sqlalchemy import UUID, Column, DateTime, Enum, String, Table, func

from exam_tutor.domain.entities.task import Task
from exam_tutor.domain.enums import DifficultEnum, ExamEnum, ExamTaskNumber, SubjectEnum
from exam_tutor.infrastructure.sqla_persistence.orm_registry import mapping_registry

tasks_table = Table(
    "tasks",
    mapping_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("exam", Enum(ExamEnum), nullable=False),
    Column("subject", Enum(SubjectEnum), nullable=False),
    Column("exam_task_number", Enum(ExamTaskNumber), nullable=False),
    Column("condition", String, nullable=False),
    Column("answer", String, nullable=False),
    Column("difficult", Enum(DifficultEnum), nullable=False),
    Column(
        "created_at",
        DateTime,
        default=func.now(),
        server_default=func.now(),
        nullable=False,
    ),
    Column("find_code", String, nullable=False),
    Column("task_sound_link", String, nullable=True),
    Column("task_file_link", String, nullable=True),
    Column("task_photo_link", String, nullable=True),
    Column("answer_video_link", String, nullable=True),
)


def map_tasks_table() -> None:
    mapping_registry.map_imperatively(
        Task,
        tasks_table,
    )
