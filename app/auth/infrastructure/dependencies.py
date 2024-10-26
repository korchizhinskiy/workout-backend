from typing import Annotated

import jwt
from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Depends
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer

from app.auth.infrastructure.exceptions import InvalidAuthenticationTokenError
from app.infrastructure.config import Settings

auth_scheme = HTTPBearer()


@inject
async def authenticate(
    token: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)],
    settings: FromDishka[Settings],
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
        return payload
