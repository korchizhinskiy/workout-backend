from collections.abc import AsyncGenerator

from dishka import (
    Provider,
    Scope,
    make_async_container,
    provide,  # type: ignore [reportUnknownVariableType]
)
from dishka.integrations.fastapi import setup_dishka
from fastapi.applications import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker

from app.infrastructure.config import Settings
from app.infrastructure.database import get_connection_url


class DishkaProvider(Provider):
    def __init__(self, config: Settings) -> None:
        super().__init__()
        self.config = config

    @provide(scope=Scope.APP)
    async def get_settings(self) -> Settings:
        return self.config

    @classmethod
    @provide(scope=Scope.APP)
    async def engine(cls, settings: Settings) -> AsyncEngine:
        database_url = get_connection_url(settings)
        database_params = {}
        return create_async_engine(database_url, **database_params)

    @classmethod
    @provide(scope=Scope.REQUEST)
    async def get_session(cls, engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
        async_session = async_sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )
        async with async_session() as session:
            yield session


def init_di(app: FastAPI) -> None:
    # Incompatible with pyright - in issue recomend change pyright to mypy
    # Issue: https://github.com/pydantic/pydantic-settings/issues/383
    config = Settings()  # type: ignore [reportCallIssue]
    container = make_async_container(DishkaProvider(config))
    setup_dishka(container, app)
