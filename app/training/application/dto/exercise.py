from uuid import UUID

from pydantic.config import ConfigDict
from pydantic.fields import Field
from pydantic.main import BaseModel


# ===== Inside Application DTO ===== #
class ExerciseDTO(BaseModel):
    id: UUID
    name: str
    description: str
    groups: list["ExerciseGroupIncludeDTO"] = Field(..., alias="exercise_groups")

    model_config = ConfigDict(from_attributes=True)


class ExerciseGroupIncludeDTO(BaseModel):
    id: UUID
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)


# ===== Creation DTO ===== #
type ExerciseGroupId = UUID


class ExerciseCreationDTO(BaseModel):
    name: str
    description: str
    exercise_groups: list[ExerciseGroupId] = Field(..., min_length=1, alias="groups")
