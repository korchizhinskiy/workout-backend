from typing import Protocol
from uuid import UUID

from app.auth.application.dto.user import UserDTO
from app.training.application.dto.exercise import ExerciseDTO

type ExerciseId = UUID


class IExerciseListQuery(Protocol):
    def execute(self, idp: UserDTO) -> list[ExerciseDTO]: ...


class IExerciseQuery(Protocol):
    async def execute(self, exercise_id: ExerciseId, idp: UserDTO) -> ExerciseDTO: ...
