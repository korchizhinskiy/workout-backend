import time

import jwt

from app.auth.application.dto.user import UserDTO
from app.infrastructure.config import Settings


class AuthService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def create_access_token(self, user_dto: UserDTO) -> str:
        return jwt.encode(
            payload={"user_id": str(user_dto.id), "expires": time.time() + 100},
            key=self.settings.certs.private_key,
            algorithm=self.settings.certs.algorithm,
        )
