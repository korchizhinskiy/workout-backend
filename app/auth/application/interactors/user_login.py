import time
from logging import getLogger

import bcrypt
import jwt
from dishka import FromDishka

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.exceptions.user import WrongPasswordError
from app.auth.application.interfaces.repository.user import IUserRepository
from app.infrastructure.config import Settings

log = getLogger(__name__)


class UserLoginInteractor:
    def __init__(self, repository: IUserRepository, settings: FromDishka[Settings]) -> None:
        self.repository = repository
        self.settings = settings

    async def execute(self, user_dto: UserLoginDTO) -> str:
        user = await self.repository.get_one(user_dto)

        if not bcrypt.checkpw(user_dto.password, user.password):
            raise WrongPasswordError
        # TODO: Set in service layer

        token = jwt.encode(
            payload={"user_id": str(user.id), "expires": time.time() + 100},
            key=self.settings.certs.private_key,
            algorithm=self.settings.certs.algorithm,
        )
        # TODO: Use Token DTO
        return token
