from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select

from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.infrastructure.models.user import User

type HashPassword = bytes
type UserId = UUID
type UserUsername = str


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, user_dto: UserRegistrationDTO) -> None:
        user = User(**user_dto.model_dump())
        self.session.add(user)
        await self.session.commit()

    async def get_user_hashed_password(self, username: UserUsername) -> bytes:
        query = select(User.password).where(User.username == username)
        hashed_password = (await self.session.scalars(query)).first()
        return hashed_password
