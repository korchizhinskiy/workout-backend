import bcrypt

from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.interfaces.repository.user import IUserRepository


class UserRegistrationInteractor:
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    async def execute(self, user_dto: UserRegistrationDTO) -> None:
        hashed_password = self.hash_password(user_dto.password)

        await self.repository.create(
            UserRegistrationDTO(**user_dto.model_dump(exclude={"password"}), password=hashed_password),
        )

    @staticmethod
    def hash_password(password: bytes) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password, salt)
