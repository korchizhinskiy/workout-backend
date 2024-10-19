from uuid import UUID

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from uuid6 import uuid7

from app.auth.infrastructure.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]

    first_name: Mapped[str]
    last_name: Mapped[str]
    second_name: Mapped[str | None]
