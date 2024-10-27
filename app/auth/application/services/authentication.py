import time

import jwt
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.auth.application.dto.user import UserDTO
from app.auth.infrastructure.models.session import AuthSession
from app.infrastructure.config import Settings


class JWTService:
    def __init__(self, settings: Settings, session: AsyncSession) -> None:
        self.settings = settings
        self.session = session

    async def create_access_token(self, user_dto: UserDTO) -> str:
        # TODO: Encrypt session id or use JWE
        sid = jwt.encode(
            payload={
                "sub": str(user_dto.id),
                "exp": time.time() + 1000,
                "crt": time.time(),
            },
            key=self.settings.certs.private_key,
            algorithm=self.settings.certs.algorithm,
        )
        async with self.session as session:
            session.add(AuthSession(jwt=sid))
            await session.commit()
        return sid
