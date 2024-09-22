from fastapi.applications import FastAPI

from app.dependencies import init_di
from app.routers.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)
init_di(app)
