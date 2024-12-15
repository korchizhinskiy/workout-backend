from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import ForeignKey

from app.auth.infrastructure.models.base import Base

if TYPE_CHECKING:
    from app.auth.infrastructure.models.user import User


class AuthSession(Base):
    __tablename__ = "auth_session"

    token: Mapped[str] = mapped_column(primary_key=True)

    user: Mapped["User"] = relationship(cascade="all, delete", back_populates="auth_sessions")
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
