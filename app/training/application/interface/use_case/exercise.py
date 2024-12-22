from typing import Protocol

from app.auth.application.dto.user import UserDTO
from app.training.application.dto.exercise import ExerciseCreationDTO, ExerciseDTO


class ExerciseCreationUseCase(Protocol):
    async def execute(self, exercise_dto: ExerciseCreationDTO, idp: UserDTO) -> ExerciseDTO: ...
