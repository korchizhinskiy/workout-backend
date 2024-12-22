from typing import Protocol
from uuid import UUID

from app.training.application.dto.exercise import ExerciseCreationDTO, ExerciseDTO

type HashPassword = bytes
type UserId = UUID
type UserUsername = str
type ExerciseId = UUID


class IExerciseRepository(Protocol):
    async def get_exercise(self, exercise_id: ExerciseId) -> ExerciseDTO | None: ...

    async def create(self, exercise_dto: ExerciseCreationDTO) -> ExerciseDTO: ...

    async def delete(self, exercise_id: ExerciseId) -> None: ...
