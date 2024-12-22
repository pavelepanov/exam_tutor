from sqlalchemy import MetaData
from sqlalchemy.orm import registry

metadata_obj: MetaData = MetaData()
mapping_registry: registry = registry(metadata=metadata_obj)
