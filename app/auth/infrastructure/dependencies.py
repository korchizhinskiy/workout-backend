from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Depends
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.strategy_options import joinedload
from sqlalchemy.sql.expression import select

from app.auth.application.dto.user import UserDTO
from app.auth.infrastructure.exceptions import InvalidAuthenticationTokenError
from app.auth.infrastructure.models.session import AuthSession

auth_scheme = HTTPBearer()


@inject
async def get_authenticated_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)],
    session: FromDishka[AsyncSession],
) -> UserDTO:
    query = select(AuthSession).options(joinedload(AuthSession.user)).where(AuthSession.token == token.credentials)
    auth_session = await session.scalar(query)

    if not auth_session:
        raise InvalidAuthenticationTokenError
    return UserDTO.model_validate(auth_session.user)
