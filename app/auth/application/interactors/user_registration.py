import bcrypt

from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.exceptions.user import UserAlreadyRegisteredError
from app.auth.application.interfaces.repository.user import IUserRepository


class UserRegistrationInteractor:
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    async def execute(self, user_dto: UserRegistrationDTO) -> None:
        registered_user = await self.repository.get_user(user_dto.username)

        if registered_user:
            raise UserAlreadyRegisteredError(username=user_dto.username)

        hashed_password = self.hash_password(user_dto.password)

        await self.repository.create(
            UserRegistrationDTO(**user_dto.model_dump(exclude={"password"}), password=hashed_password),
        )

    # TODO: Set function in another module (may be using on registration, on login and change password)
    # https://github.com/korchizhinskiy/workout-backend/issues/12
    @staticmethod
    def hash_password(password: bytes) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password, salt)
