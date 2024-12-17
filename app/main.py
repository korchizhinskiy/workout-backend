from fastapi.applications import FastAPI

from app.auth.presentation.api.routers.auth import router as auth_router
from app.auth.presentation.exceptions import setup_exception_handlers
from app.infrastructure.ioc.dependencies import init_di
from app.infrastructure.log import configure_logging
from app.user.presentation.api.routers.user_profile import router as user_router

# TODO: Set main router by package layer (in init module)

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
setup_exception_handlers(app)
init_di(app)

configure_logging()
