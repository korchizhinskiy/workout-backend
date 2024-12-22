from typing import Protocol
from uuid import UUID

from app.auth.application.dto.user import UserDTO
from app.training.application.dto.exercise_group import ExerciseGroupDTO

type ExerciseGroupId = UUID


class IExerciseGroupListQuery(Protocol):
    async def execute(self, idp: UserDTO) -> list[ExerciseGroupDTO]: ...


class IExerciseGroupQuery(Protocol):
    async def execute(self, exercise_group_id: ExerciseGroupId, idp: UserDTO) -> ExerciseGroupDTO: ...
