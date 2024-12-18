from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid6 import uuid7

from app.training.infrastructure.models.base import Base

if TYPE_CHECKING:
    from app.training.infrastructure.models.exercise import Exercise
    from app.training.infrastructure.models.exercise_group import ExerciseGroup


class ExerciseExerciseGroupAssociation(Base):
    __tablename__ = "exercise_exercise_group_association"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)

    exercise_id: Mapped[UUID] = mapped_column(ForeignKey("exercise.id"))
    exercise_group_id: Mapped[UUID] = mapped_column(ForeignKey("exercise_group.id"))

    exercise: Mapped["Exercise"] = relationship(back_populates="exercise_group_associations")
    exercise_group: Mapped["ExerciseGroup"] = relationship(back_populates="exercise_associations")
