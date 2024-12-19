from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi.applications import FastAPI

from app.infrastructure.config import Settings
from app.infrastructure.ioc.providers import (
    ApplicationConfigProvider,
    AuthInteractorProvider,
    AuthRepositoryProvider,
    AuthServiceProvider,
    SQLAlchemyProvider,
)
from app.infrastructure.ioc.providers.training.query import QueryProvider as TrainingQueryProvider
from app.infrastructure.ioc.providers.user.query import QueryProvider as UserQueryProvider


def init_di(app: FastAPI) -> None:
    # Incompatible with pyright - in issue recomend change pyright to mypy
    # Issue: https://github.com/pydantic/pydantic-settings/issues/383
    container = make_async_container(
        ApplicationConfigProvider(),
        SQLAlchemyProvider(),
        AuthRepositoryProvider(),
        AuthInteractorProvider(),
        AuthServiceProvider(),
        UserQueryProvider(),
        TrainingQueryProvider(),
        context={Settings: Settings()},  # type: ignore [reportCallIssue]
    )
    setup_dishka(container, app)
