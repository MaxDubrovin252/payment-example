from fastapi import FastAPI
from core.config import settings
import uvicorn


app = FastAPI()

if __name__=="__main__":
    uvicorn.run(
        "main:app",
        port=settings.srv.port,
        host=settings.srv.host,
        reload=True,
    )