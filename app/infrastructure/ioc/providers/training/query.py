from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.training.application.interface.query.exercise import IExerciseQuery
from app.training.infrastructure.query.exercise import ExerciseQuery


class QueryProvider(Provider):
    user_profile_query = provide(
        ExerciseQuery,
        provides=IExerciseQuery,
        scope=Scope.REQUEST,
    )
