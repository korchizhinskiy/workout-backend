from pathlib import Path, PosixPath

from pydantic.functional_validators import field_validator
from pydantic.main import BaseModel
from pydantic.types import FilePath
from pydantic_settings.main import BaseSettings, SettingsConfigDict

type PublicKeyPath = FilePath
type PrivateKeyPath = FilePath
type Certificate = str
type AlgorithmName = str

BASE_DIR = Path(__file__).parent.parent


class CryptoModel(BaseModel):
    public_key: PublicKeyPath
    private_key: PrivateKeyPath
    algorithm: AlgorithmName = "RS256"

    @field_validator("public_key", "private_key", mode="after")
    @classmethod
    def load_file_content(cls, value: PosixPath) -> Certificate:
        return Path(BASE_DIR / value).read_text(encoding="utf-8").strip()


class Settings(BaseSettings):
    certs: CryptoModel
    model_config = SettingsConfigDict(env_file=(".env",), env_nested_delimiter="__")
