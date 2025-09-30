from repository.user import create_user
from sqlalchemy.ext.asyncio import AsyncSession
from service.passwords import hash_password
async def create_new_user(
    session:AsyncSession,
    username:str,
    password:str
):
    hash_pass = hash_password(password=password)
    new_user = await create_user(session=session,username=username,password=hash_pass)
    return new_user
    