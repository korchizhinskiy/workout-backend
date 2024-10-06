from dishka.integrations.fastapi import FromDishka, inject
from fastapi.routing import APIRouter

from app.application.dto.registration import UserRegistrationDTO
from app.application.interactors.user_registration import UserRegistrationInteractor
from app.presentation.schemas.registration import UserRegistrationInputSchema

router = APIRouter(prefix="/auth")


@router.post("/registration")
@inject
async def registration(
    user_data: UserRegistrationInputSchema,
    interactor: FromDishka[UserRegistrationInteractor],
) -> UserRegistrationInputSchema:
    await interactor.execute(
        UserRegistrationDTO(
            username=user_data.username,
            password=user_data.password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            second_name=user_data.second_name,
        ),
    )
    return user_data
