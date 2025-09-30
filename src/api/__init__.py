from fastapi import APIRouter
from .user import router as auth_router

router = APIRouter(prefix="/api/v1")
router.include_router(router=auth_router)
