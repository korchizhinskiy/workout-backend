from dishka.integrations.fastapi import FromDishka, inject
from fastapi.routing import APIRouter

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.interactors.user_login import UserLoginInteractor
from app.auth.application.interactors.user_registration import UserRegistrationInteractor
from app.auth.presentation.schemas.login import UserLoginInputSchema
from app.auth.presentation.schemas.registration import UserRegistrationInputSchema

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


@router.post("/login")
@inject
async def login(
    user_data: UserLoginInputSchema,
    interactor: FromDishka[UserLoginInteractor],
) -> UserLoginInputSchema:
    await interactor.execute(
        UserLoginDTO(username=user_data.username, password=user_data.password),
    )
    return user_data


# @router.post("/refresh")
# @inject
# async def registration(
#     user_data: UserLoginInputSchema,
#     interactor: FromDishka[UserLoginInteractor],
# ) -> UserRegistrationInputSchema:
#     pass
