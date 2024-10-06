from typing import Protocol

from app.application.dto.registration import UserRegistrationDTO


class IUserRepository(Protocol):
    async def create(self, user_dto: UserRegistrationDTO) -> None:
        pass
