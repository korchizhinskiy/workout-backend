from logging import getLogger

import bcrypt

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.exceptions.user import WrongPasswordError
from app.auth.application.interfaces.repository.user import IUserRepository
from app.auth.application.services.authentication import JWTService

log = getLogger(__name__)


class UserLoginInteractor:
    def __init__(self, repository: IUserRepository, auth_service: JWTService) -> None:
        self.repository = repository
        self.auth_service = auth_service

    async def execute(self, user_dto: UserLoginDTO) -> str:
        user = await self.repository.get_one(user_dto)

        if not bcrypt.checkpw(user_dto.password, user.password):
            raise WrongPasswordError
        # TODO: Use Token DTO
        return self.auth_service.create_access_token(user)
