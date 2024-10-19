from typing import Protocol
from uuid import UUID

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.dto.user import UserDTO

type HashPassword = bytes
type UserId = UUID
type UserUsername = str


class IUserRepository(Protocol):
    async def get_one(self, user_dto: UserLoginDTO) -> UserDTO: ...

    async def create(self, user_dto: UserRegistrationDTO) -> None: ...

    async def get_user_hashed_password(self, username: UserUsername) -> bytes: ...
