from typing import Annotated

import jwt
from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Depends
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import select

from app.auth.infrastructure.exceptions import InvalidAuthenticationTokenError, SessionIsExpiredError
from app.auth.infrastructure.models.session import AuthSession
from app.infrastructure.config import Settings

auth_scheme = HTTPBearer()


@inject
async def authenticate(
    token: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)],
    settings: FromDishka[Settings],
    session: FromDishka[AsyncSession],
) -> dict:
    try:
        payload = jwt.decode(
            jwt=token.credentials,
            key=settings.certs.public_key,
            algorithms=[settings.certs.algorithm],
        )
    except jwt.ExpiredSignatureError as error:
        pass
        # TODO: Check by session id and recookie or unlogin user
    except jwt.InvalidTokenError as error:
        raise InvalidAuthenticationTokenError from error
    else:
        async with session:
            query = select(AuthSession).where(AuthSession.jwt == token.credentials)
            auth_session = await session.scalar(query)
            if not auth_session:
                raise SessionIsExpiredError

        return payload
