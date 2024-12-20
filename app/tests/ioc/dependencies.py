from pydantic_settings.main import BaseSettings, SettingsConfigDict

from app.infrastructure.config import CommonSettings, CryptoSettings, DatabaseConnectionSettings


class MockSettings(BaseSettings):
    certs: CryptoSettings
    db_connection: DatabaseConnectionSettings
    common: CommonSettings
    model_config = SettingsConfigDict(env_file=(".env.test",), env_nested_delimiter="__", str_to_lower=True)
