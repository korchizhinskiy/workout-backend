from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.infrastructure.config import Settings


class ApplicationConfigProvider(Provider):
    def __init__(self, config: Settings) -> None:
        super().__init__()
        self.config = config

    @provide(scope=Scope.APP)
    async def get_settings(self) -> Settings:
        return self.config
