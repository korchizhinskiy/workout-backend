import pytest
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import insert

from app.training.infrastructure.models.exercise import Exercise


@pytest.fixture
async def fixture_exercise(session: AsyncSession) -> None:
    stmt = insert(Exercise).values(name="Жим лежа", description="Жим лежа - это упражение")
    await session.execute(stmt)
