from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.infrastructure.repository.user import UserRepository


class RepositoryProvider(Provider):
    @classmethod
    @provide(scope=Scope.REQUEST)
    def provide_user_repository(cls, session: AsyncSession) -> UserRepository:
        return UserRepository(session)
