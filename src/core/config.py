from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os



class DataBaseSettings(BaseModel):
    url:str = os.getenv("DB_URL")
    echo:bool = False
    echo_pool:bool = False
    max_overflow:int = 10
    
    
class JWTSettings(BaseModel):
    secret_key:str = os.getenv("JWT_SECRET_KEY")
    algo:str = os.getenv("ALGO")
    
    
class PaymentSettings(BaseSettings):
    secret_key:str = os.getenv("SECRET_KEY")
    
    
class ServerSettings(BaseSettings):
    port:int = 8080
    host:str = "0.0.0.0"
    
class Settings(BaseSettings):
    db:DataBaseSettings = DataBaseSettings()
    jwt:JWTSettings = JWTSettings()
    payment:PaymentSettings = PaymentSettings()
    srv:ServerSettings = ServerSettings()
    
    
settings = Settings()