from sqlalchemy import DATETIME, UUID, Column, Enum, ForeignKey, String, Table, func

from exam_tutor.domain.enums import DifficultEnum, ExamEnum, ExamTaskNumber, SubjectEnum
from exam_tutor.infrastructure.sqla_persistence.orm_registry import metadata_obj

tasks_table = Table(
    "tasks",
    metadata_obj,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("exam", Enum(ExamEnum)),
    Column("subject", Enum(SubjectEnum)),
    Column("exam_task_number", Enum(ExamTaskNumber)),
    Column("condition", String),
    Column("answer", String),
    Column("difficult", Enum(DifficultEnum)),
    Column("created_at", DATETIME, default=func.now()),
    Column("task_sound_id", ForeignKey("task_sound.id"), nullable=False),
    Column("task_file_id", ForeignKey("task_files.id"), nullable=False),
    Column("task_photo_id", ForeignKey("task_photos.id"), nullable=False),
    Column("answer_video_id", ForeignKey("answer_videos.id"), nullable=False),
)
