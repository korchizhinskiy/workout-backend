import pytest
import starlette.status as status_code
from httpx import AsyncClient


@pytest.mark.asyncio(loop_scope="session")
# @pytest.mark.usefixtures("fixture_exercise")
async def test_get_exercise_without_authentication(client: AsyncClient) -> None:
    response = await client.get("training/exercises")
    assert response.status_code == status_code.HTTP_403_FORBIDDEN


@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.usefixtures("fixture_exercise")
async def test_get_exercises(client: AsyncClient) -> None:
    response = await client.get("training/exercises")
    assert response.status_code == status_code.HTTP_403_FORBIDDEN
