from fastapi.routing import APIRouter

from .model import router as model_router

router = APIRouter(prefix="/api")
router.include_router(model_router)
