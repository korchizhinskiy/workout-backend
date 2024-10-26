from sqlalchemy.orm import Mapped, mapped_column

from app.auth.infrastructure.models.base import Base


class AuthSession(Base):
    __tablename__ = "auth_sessions"

    jwt: Mapped[str] = mapped_column(primary_key=True)
