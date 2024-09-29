from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.application.interactors.user_registration import UserRegistrationInteractor
from app.infrastructure.repository.user import UserRepository


class InteractorProvider(Provider):
    @classmethod
    @provide(scope=Scope.REQUEST)
    async def provide_user_registration_interactor(cls, repository: UserRepository) -> UserRegistrationInteractor:
        return UserRegistrationInteractor(repository)
