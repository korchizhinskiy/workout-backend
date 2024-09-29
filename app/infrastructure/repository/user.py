from sqlalchemy.ext.asyncio.session import AsyncSession


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    def create(self) -> None:
        pass
