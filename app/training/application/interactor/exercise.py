from typing import final

from app.auth.application.dto.user import UserDTO
from app.training.application.dto.exercise import ExerciseCreationDTO, ExerciseDTO
from app.training.application.interface.repository.exercise import IExerciseRepository


@final
class ExerciseCreationInteractor:
    def __init__(self, repository: IExerciseRepository) -> None:
        self.repository = repository

    async def execute(self, exercise_dto: ExerciseCreationDTO, idp: UserDTO) -> ExerciseDTO:
        exercise = await self.repository.create(exercise_dto)
        return ExerciseDTO.model_validate(exercise)
