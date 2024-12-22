from fastapi.routing import APIRouter

from .exercise import router as exercise_router
from .exercise_group import router as exercise_group_router

router = APIRouter(tags=["Training"], prefix="/training")
router.include_router(exercise_router)
router.include_router(exercise_group_router)
