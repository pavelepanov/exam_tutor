from sqlalchemy import UUID, Column, String, Table

from exam_tutor.infrastructure.sqla_persistence.orm_registry import mapping_registry

task_sounds_table = Table(
    "task_sounds",
    mapping_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("link", String),
)
