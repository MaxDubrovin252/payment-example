from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from core.config import settings

class DataBaseHelper:
    def __init__(self,url:str,echo:bool=False,echo_pool:bool=False,max_overflow:int=10):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
        )
        
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
            
        )
        
    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            
            
db_helper = DataBaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    max_overflow=settings.db.max_overflow,
)