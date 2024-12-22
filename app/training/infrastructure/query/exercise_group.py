from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import select

from app.auth.application.dto.user import UserDTO
from app.training.application.dto.exercise_group import ExerciseGroupDTO
from app.training.application.interface.query.exercise_group import IExerciseGroupListQuery, IExerciseGroupQuery
from app.training.infrastructure.exception import ResourseNotFoundError
from app.training.infrastructure.models.exercise_group import ExerciseGroup

type ExerciseGroupId = UUID


class ExerciseGroupListQuery(IExerciseGroupListQuery):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def execute(self, idp: UserDTO) -> list[ExerciseGroupDTO]:  # noqa: ARG002
        query = select(ExerciseGroup)
        exercises = await self.session.scalars(query)
        return [ExerciseGroupDTO.model_validate(exercise) for exercise in exercises]


class ExerciseGroupQuery(IExerciseGroupQuery):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def execute(self, exercise_group_id: ExerciseGroupId, idp: UserDTO) -> ExerciseGroupDTO:  # noqa: ARG002
        query = select(ExerciseGroup).where(ExerciseGroup.id == exercise_group_id)
        result = await self.session.scalar(query)
        if result is None:
            raise ResourseNotFoundError(resourse_identity=str(exercise_group_id))
        return ExerciseGroupDTO.model_validate(result)
