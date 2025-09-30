from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User



async def get_user(
    session:AsyncSession,
    username:str
)->User|None:
    stmt = select(User).where(User.username==username)
    res = await session.execute(statement=stmt)
    user = res.scalars().one_or_none()
    return user

async def create_user(
    session:AsyncSession,
    username:str,
    password:bytes,
)->User|None:
    user_exist = get_user(
        session=session,
        username=username
    )
    if user_exist:
        await session.rollback()
        return None
    
    new_user = User(username=username,password=password)
    session.add(new_user)
    await session.commit()
    return new_user