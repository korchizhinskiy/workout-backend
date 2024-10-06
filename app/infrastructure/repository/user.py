from sqlalchemy.ext.asyncio.session import AsyncSession

from app.application.dto.registration import UserRegistrationDTO
from app.infrastructure.models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, user_dto: UserRegistrationDTO) -> None:
        user = User(**user_dto.model_dump())
        self.session.add(user)
        await self.session.commit()
