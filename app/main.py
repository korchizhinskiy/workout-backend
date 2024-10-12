from fastapi.applications import FastAPI

from app.infrastructure.ioc.dependencies import init_di
from app.infrastructure.log import configure_logging
from app.presentation.api.routers.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)
init_di(app)

configure_logging()
