from typing import Protocol
from uuid import UUID

from app.auth.application.dto.registration import UserRegistrationDTO

type HashPassword = bytes
type UserId = UUID
type UserUsername = str


class IUserRepository(Protocol):
    async def create(self, user_dto: UserRegistrationDTO) -> None: ...

    async def get_user_hashed_password(self, username: UserUsername) -> bytes: ...
