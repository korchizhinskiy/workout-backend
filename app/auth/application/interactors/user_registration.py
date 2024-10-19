import bcrypt

from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.interfaces.repository.user import IUserRepository


class UserRegistrationInteractor:
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    async def execute(self, user_dto: UserRegistrationDTO) -> None:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user_dto.password, salt)

        await self.repository.create(
            UserRegistrationDTO(**user_dto.model_dump(exclude={"password"}), password=hashed_password),
        )
