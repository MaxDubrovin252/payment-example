from fastapi import APIRouter,Depends,HTTPException,Form
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper,User
from service.user import user_service
router = APIRouter()

router.post("sign-up")
async def sign_up(
    user_form:User = Form(),
    session:AsyncSession = Depends(db_helper.session_dependency),
):
    new_user = await user_service.create_new_user(
        session=session,
        username=user_form.username,
        password=user_form.password,
    )
    if new_user is None:
        raise HTTPException(status_code=400,detail=f"user {user_form.username} was already exist")
    return new_user
