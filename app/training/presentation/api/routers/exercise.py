from typing import Annotated
from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter

from app.auth.application.dto.user import UserDTO
from app.auth.infrastructure.dependencies import get_authenticated_user
from app.training.application.dto.exercise import ExerciseCreationDTO, ExerciseDTO
from app.training.application.interface.query.exercise import IExerciseListQuery, IExerciseQuery
from app.training.application.interface.use_case.exercise import ExerciseCreationUseCase
from app.training.presentation.schemas.exercise import ExerciseOutputSchema

router = APIRouter()


@router.get("/exercises", response_model=list[ExerciseOutputSchema])
@inject
async def get_exercises(
    idp: Annotated[UserDTO, Depends(get_authenticated_user)],
    query: FromDishka[IExerciseListQuery],
) -> list[ExerciseDTO]:
    return await query.execute(idp)


@router.get("/exercises/{exercise_id}", response_model=ExerciseOutputSchema)
@inject
async def get_exercise_by_id(
    exercise_id: UUID,
    idp: Annotated[UserDTO, Depends(get_authenticated_user)],
    query: FromDishka[IExerciseQuery],
) -> ExerciseDTO:
    return await query.execute(exercise_id, idp)


@router.post("/exercises")
@inject
async def create_exercise(
    exercise_dto: ExerciseCreationDTO,
    interactor: FromDishka[ExerciseCreationUseCase],
    idp: Annotated[UserDTO, Depends(get_authenticated_user)],
) -> ExerciseDTO:
    return await interactor.execute(exercise_dto, idp)
