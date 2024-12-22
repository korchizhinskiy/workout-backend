from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql.expression import select

from app.training.application.dto.exercise import ExerciseCreationDTO, ExerciseDTO
from app.training.application.interface.repository.exercise import IExerciseRepository
from app.training.infrastructure.models.exercise import Exercise
from app.training.infrastructure.models.exercise_exercise_group_association import ExerciseExerciseGroupAssociation

type HashPassword = bytes
type UserId = UUID
type UserUsername = str
type ExerciseId = UUID


class ExerciseRepository(IExerciseRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_exercise(self, exercise_id: ExerciseId) -> ExerciseDTO | None:
        exercise_query = select(Exercise).where(Exercise.id == exercise_id)
        exercise = await self.session.scalar(exercise_query)

        if not exercise:
            return None

        return ExerciseDTO.model_validate(exercise)

    async def create(self, exercise_dto: ExerciseCreationDTO) -> ExerciseDTO:
        exercise_groups_for_create = exercise_dto.exercise_groups
        exercise_for_create = Exercise(**exercise_dto.model_dump(exclude={"exercise_groups"}))

        # Create relation models = exercise_group
        for group in exercise_groups_for_create:
            association = ExerciseExerciseGroupAssociation(exercise=exercise_for_create, exercise_group_id=group)
            exercise_for_create.exercise_group_associations.append(association)
        self.session.add(exercise_for_create)

        await self.session.commit()
        await self.session.refresh(exercise_for_create)

        exercise_query = (
            select(Exercise)
            .options(selectinload(Exercise.exercise_groups))
            .where(Exercise.id == exercise_for_create.id)
        )
        return ExerciseDTO.model_validate(await self.session.scalar(exercise_query))

    async def delete(self, exercise_id: ExerciseId) -> None:
        pass
