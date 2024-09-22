from dishka import (
    Provider,
    Scope,
    make_async_container,
    provide,  # type: ignore [reportUnknownVariableType]
)
from dishka.integrations.fastapi import setup_dishka
from fastapi.applications import FastAPI

from app.config import Settings


class DishkaProvider(Provider):
    @provide(scope=Scope.APP)
    @classmethod
    async def get_settings(cls) -> Settings:
        # Incompatible with pyright - in issue recomend change pyright to mypy
        # Issue: https://github.com/pydantic/pydantic-settings/issues/383
        return Settings()  # type: ignore [reportCallIssue]


provider = DishkaProvider()


def init_di(app: FastAPI) -> None:
    container = make_async_container(DishkaProvider())
    setup_dishka(container, app)
