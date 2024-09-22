import time

import jwt
from dishka.integrations.fastapi import FromDishka, inject
from fastapi import HTTPException, status
from fastapi.routing import APIRouter
from jwt.exceptions import DecodeError, InvalidSignatureError

from app.config import Settings

router = APIRouter(prefix="/auth")


@router.post("/registration")
@inject
async def registration(settings: FromDishka[Settings]) -> str:
    payload = {
        "user_id": 123,
        "expires": time.time() + 100,
    }
    token = jwt.encode(
        payload=payload,
        key=settings.certs.private_key,
        algorithm=settings.certs.algorithm,
    )
    return token


@router.post("/check")
@inject
async def check(token: str, settings: FromDishka[Settings]) -> str:
    try:
        token = jwt.decode(
            token,
            key=settings.certs.public_key,
            algorithms=[settings.certs.algorithm],
        )
    except InvalidSignatureError as signature_error:
        # TODO: Set custom exception.
        raise HTTPException(
            detail="Invalid access token.", status_code=status.HTTP_403_FORBIDDEN
        ) from signature_error
    except DecodeError as decode_error:
        raise HTTPException(
            detail="Token is broken.", status_code=status.HTTP_400_BAD_REQUEST
        ) from decode_error
    return "ds"
