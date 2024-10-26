from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.auth.application.interactors.user_login import UserLoginInteractor
from app.auth.application.interactors.user_registration import UserRegistrationInteractor

# TODO: Set providers by modules


class InteractorProvider(Provider):
    user_registration_interactor = provide(
        UserRegistrationInteractor,
        provides=UserRegistrationInteractor,
        scope=Scope.REQUEST,
    )
    user_login_interactor = provide(
        UserLoginInteractor,
        provides=UserLoginInteractor,
        scope=Scope.REQUEST,
    )
