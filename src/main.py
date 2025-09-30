from fastapi import FastAPI
from core.config import settings
from api import router 
import uvicorn


app = FastAPI()
app.include_router(router=router)

if __name__=="__main__":
    uvicorn.run(
        "main:app",
        port=settings.srv.port,
        host=settings.srv.host,
        reload=True,
    )