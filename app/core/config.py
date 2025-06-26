from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Flower Planning Backend"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = "your-secret-key-keep-it-secret"  # Change in production!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./data/flowers.db"

    class Config:
        case_sensitive = True

settings = Settings()

# Ensure data directory exists
os.makedirs("./data", exist_ok=True) 