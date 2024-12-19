from uuid import UUID

from pydantic import BaseModel
from pydantic.config import ConfigDict


class ExerciseOutputSchema(BaseModel):
    id: UUID
    name: str
    description: str
    groups: list["ExerciseGroupIncludeOutputShema"]

    model_config = ConfigDict(from_attributes=True)


class ExerciseGroupIncludeOutputShema(BaseModel):
    id: UUID
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)
