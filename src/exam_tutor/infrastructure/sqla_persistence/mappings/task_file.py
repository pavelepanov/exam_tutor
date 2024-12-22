from sqlalchemy import UUID, Column, String, Table

from exam_tutor.infrastructure.sqla_persistence.orm_registry import metadata_obj

task_files_table = Table(
    "task_files",
    metadata_obj,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("link", String),
)
