from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.exceptions.user import UserAlreadyRegisteredError
from app.auth.application.interfaces.repository.user import IUserRepository
from app.auth.application.services.security import hash_password


class UserRegistrationInteractor:
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    async def execute(self, user_dto: UserRegistrationDTO) -> None:
        registered_user = await self.repository.get_user(user_dto.username)

        if registered_user:
            raise UserAlreadyRegisteredError(username=user_dto.username)

        hashed_password = hash_password(user_dto.password)

        await self.repository.create(
            UserRegistrationDTO(**user_dto.model_dump(exclude={"password"}), password=hashed_password),
        )
