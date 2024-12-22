from typing import Protocol

from app.auth.application.dto.user import UserDTO
from app.training.application.dto.exercise_group import ExerciseGroupCreationDTO, ExerciseGroupDTO


class ExerciseCreationUseCase(Protocol):
    def execute(self, exercise_dto: ExerciseGroupCreationDTO, idp: UserDTO) -> ExerciseGroupDTO: ...
