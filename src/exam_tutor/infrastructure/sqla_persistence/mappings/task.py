from sqlalchemy import DateTime, UUID, Column, Enum, ForeignKey, String, Table, func, Integer

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
    Column("created_at", DateTime, default=func.now(), server_default=func.now(), nullable=False),
    Column("find_code", String, nullable=False),
    Column("task_sound_link", String, nullable=True),
    Column("task_file_link", String, nullable=True),
    Column("task_photo_link", String, nullable=True),
    Column("answer_video_link", String, nullable=True)
)


def map_tasks_table() -> None:
    mapping_registry.map_imperatively(
        Task,
        tasks_table,
        properties={
            "id": tasks_table.c.id,
            "exam": tasks_table.c.exam,
            "subject": tasks_table.c.subject,
            "exam_task_number": tasks_table.c.exam_task_number,
            "condition": tasks_table.c.condition,
            "answer": tasks_table.c.answer,
            "difficult": tasks_table.c.difficult,
            "created_at": tasks_table.c.created_at,
            "find_code": tasks_table.c.find_code,
            "task_sound_link": tasks_table.c.task_sound_link,
            "task_file_link": tasks_table.c.task_file_link,
            "task_photo_link": tasks_table.c.task_photo_link,
            "answer_video_link": tasks_table.c.answer_video_link,
        }
    )
