from uuid import UUID

from pydantic.config import ConfigDict
from pydantic.main import BaseModel


# ===== Inside Application DTO ===== #
class ExerciseGroupDTO(BaseModel):
    id: UUID
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)


# ===== Creation DTO ===== #
class ExerciseGroupCreationDTO(BaseModel):
    name: str
    description: str
