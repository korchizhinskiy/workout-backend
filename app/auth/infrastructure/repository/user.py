from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select
from sqlalchemy.sql.expression import exists

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.dto.user import UserDTO
from app.auth.application.exceptions.user import UserNotFoundError
from app.auth.infrastructure.models.user import User

type HashPassword = bytes
type UserId = UUID
type UserUsername = str


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_one(self, user_dto: UserLoginDTO) -> UserDTO:
        user_query = select(User).where(User.username == user_dto.username)
        user = await self.session.scalar(user_query)

        if not user:
            raise UserNotFoundError(username=user_dto.username)
        return UserDTO.model_validate(user)

    async def create(self, user_dto: UserRegistrationDTO) -> None:
        user = User(**user_dto.model_dump())
        self.session.add(user)
        await self.session.commit()

    async def get_user_hashed_password(self, username: UserUsername) -> bytes:
        user_exist_query = select(exists().where(User.username == username))
        exist_user = await self.session.scalar(user_exist_query)

        if not exist_user:
            raise UserNotFoundError(username=username)

        user_password_query = select(User.password).where(User.username == username)
        return (await self.session.scalars(user_password_query)).one()
