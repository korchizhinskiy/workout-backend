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
    def __init__(self, config: Settings) -> None:
        super().__init__()
        self.config = config

    @provide(scope=Scope.APP)
    async def get_settings(self) -> Settings:
        return self.config


def init_di(app: FastAPI) -> None:
    # Incompatible with pyright - in issue recomend change pyright to mypy
    # Issue: https://github.com/pydantic/pydantic-settings/issues/383
    config = Settings()  # type: ignore [reportCallIssue]
    container = make_async_container(DishkaProvider(config))
    setup_dishka(container, app)
