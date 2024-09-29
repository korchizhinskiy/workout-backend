from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi.applications import FastAPI

from app.infrastructure.config import Settings
from app.infrastructure.ioc.providers.database import SQLAlchemyProvider
from app.infrastructure.ioc.providers.interactor import InteractorProvider
from app.infrastructure.ioc.providers.repository import RepositoryProvider


def init_di(app: FastAPI) -> None:
    # Incompatible with pyright - in issue recomend change pyright to mypy
    # Issue: https://github.com/pydantic/pydantic-settings/issues/383
    config = Settings()  # type: ignore [reportCallIssue]
    container = make_async_container(SQLAlchemyProvider(config), RepositoryProvider(), InteractorProvider())
    setup_dishka(container, app)
