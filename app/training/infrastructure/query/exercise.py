from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.strategy_options import selectinload
from sqlalchemy.sql.expression import select

from app.auth.application.dto.user import UserDTO
from app.training.application.dto.exercise import ExerciseDTO
from app.training.application.interface.query.exercise import IExerciseListQuery, IExerciseQuery
from app.training.infrastructure.exception import ResourseNotFoundError
from app.training.infrastructure.models.exercise import Exercise

type ExerciseId = UUID


class ExerciseListQuery(IExerciseListQuery):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def execute(self, idp: UserDTO) -> list[ExerciseDTO]:  # noqa: ARG002
        query = select(Exercise).options(selectinload(Exercise.exercise_groups))
        exercises = await self.session.scalars(query)
        return [ExerciseDTO.model_validate(exercise) for exercise in exercises]


class ExerciseQuery(IExerciseQuery):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def execute(self, exercise_id: ExerciseId, idp: UserDTO) -> ExerciseDTO:  # noqa: ARG002
        query = select(Exercise).options(selectinload(Exercise.exercise_groups)).where(Exercise.id == exercise_id)
        result = await self.session.scalar(query)
        if result is None:
            raise ResourseNotFoundError(resourse_identity=str(exercise_id))
        return ExerciseDTO.model_validate(result)
