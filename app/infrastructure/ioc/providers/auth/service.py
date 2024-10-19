from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.auth.application.services.authentication import AuthService


class ServiceProvider(Provider):
    user_login_interactor = provide(
        AuthService,
        provides=AuthService,
        scope=Scope.REQUEST,
    )
