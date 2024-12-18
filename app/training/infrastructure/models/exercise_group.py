from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from uuid6 import uuid7

from app.training.infrastructure.models.base import Base

if TYPE_CHECKING:
    from app.training.infrastructure.models.exercise import Exercise
    from app.training.infrastructure.models.exercise_exercise_group_association import ExerciseExerciseGroupAssociation


class ExerciseGroup(Base):
    __tablename__ = "exercise_group"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)

    name: Mapped[str]
    description: Mapped[str]

    exercises: Mapped[list["Exercise"]] = relationship(
        secondary="exercise_exercise_group_association",
        back_populates="exercise_groups",
    )
    exercise_associations: Mapped[list["ExerciseExerciseGroupAssociation"]] = relationship(
        back_populates="exercise_group",
    )
