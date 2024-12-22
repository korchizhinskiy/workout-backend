from typing import Annotated
from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from uuid import UUID

from app.auth.application.dto.user import UserDTO
from app.auth.infrastructure.dependencies import get_authenticated_user
from app.training.application.dto.exercise_group import ExerciseGroupCreationDTO, ExerciseGroupDTO
from app.training.application.interface.query.exercise_group import IExerciseGroupListQuery, IExerciseGroupQuery

router = APIRouter()


@router.get("/exercise_groups")
@inject
async def get_exercise_groups(
    query: FromDishka[IExerciseGroupListQuery],
    idp: Annotated[UserDTO, Depends(get_authenticated_user)],
) -> list[ExerciseGroupDTO]:
    return await query.execute(idp)


@router.get("/exercise_groups/{exercise_group_id}")
@inject
async def get_exercise_group_by_id(
    exercise_group_id: UUID,
    query: FromDishka[IExerciseGroupQuery],
    idp: Annotated[UserDTO, Depends(get_authenticated_user)],
) -> ExerciseGroupDTO:
    return await query.execute(exercise_group_id, idp)


@router.post("/exercise_groups")
@inject
async def create_exercise_group(
    exercice_group_dto: ExerciseGroupCreationDTO,
) -> dict:
    return {}
