from pathlib import PosixPath

from pydantic.functional_validators import field_validator
from pydantic.main import BaseModel
from pydantic.types import FilePath
from pydantic_settings.main import BaseSettings, SettingsConfigDict

type PublicKeyPath = FilePath
type PrivateKeyPath = FilePath
type Certificate = str


class CryptoModel(BaseModel):
    public_key: PublicKeyPath
    private_key: PrivateKeyPath

    @field_validator("public_key", "private_key")
    @classmethod
    def load_public_key(cls, value: PosixPath) -> Certificate:
        return value.read_text().strip()


class Settings(BaseSettings):
    certs: CryptoModel
    model_config = SettingsConfigDict(env_file=(".env",), env_nested_delimiter="__")
