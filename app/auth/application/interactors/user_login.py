from logging import getLogger

import bcrypt

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.interfaces.repository.user import IUserRepository
from dishka import FromDishka
import jwt

from app.infrastructure.config import Settings

log = getLogger(__name__)


class UserLoginInteractor:
    def __init__(self, repository: IUserRepository, settings: FromDishka[Settings]) -> str:
        self.repository = repository
        self.settings = settings

    async def execute(self, user_dto: UserLoginDTO) -> None:
        hashed_password = await self.repository.get_user_hashed_password(user_dto.username)

        if bcrypt.checkpw(user_dto.password, hashed_password):
            log.debug("User with username=%s sent right password.", user_dto.username)
