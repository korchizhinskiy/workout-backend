from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.auth.application.interactors.user_login import UserLoginInteractor
from app.auth.application.interactors.user_registration import UserRegistrationInteractor
from app.auth.infrastructure.repository.user import UserRepository
from app.infrastructure.config import Settings

# TODO: Set providers by modules


class InteractorProvider(Provider):
    @classmethod
    @provide(scope=Scope.REQUEST)
    async def provide_user_registration_interactor(cls, repository: UserRepository) -> UserRegistrationInteractor:
        return UserRegistrationInteractor(repository)

    @classmethod
    @provide(scope=Scope.REQUEST)
    async def provide_user_login_interactor(cls, repository: UserRepository, settings: Settings) -> UserLoginInteractor:
        return UserLoginInteractor(repository, settings)
