from pathlib import Path, PosixPath

from pydantic.functional_validators import field_validator
from pydantic.main import BaseModel
from pydantic_settings.main import BaseSettings, SettingsConfigDict

type PublicKeyPath = str
type PrivateKeyPath = str
type Certificate = str
type AlgorithmName = str

BASE_DIR = Path(__file__).parent.parent


class DatabaseConnection(BaseModel):
    database_user: str
    database_name: str
    database_password: str
    database_host: str
    database_port: int


class CryptoModel(BaseModel):
    public_key: PublicKeyPath
    private_key: PrivateKeyPath
    algorithm: AlgorithmName = "RS256"

    @field_validator("public_key", "private_key", mode="before")
    @classmethod
    def load_file_content(cls, value: PosixPath) -> Certificate:
        try:
            return Path(BASE_DIR / value).read_text(encoding="utf-8").strip()
        except IsADirectoryError as error:
            raise ValueError("You must define path to file, not to directory.") from error
        except FileNotFoundError as error:
            raise ValueError("This path ot file is not found.") from error


class Settings(BaseSettings):
    certs: CryptoModel
    db_connection: DatabaseConnection
    model_config = SettingsConfigDict(env_file=(".env",), env_nested_delimiter="__")
