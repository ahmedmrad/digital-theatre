# src/config.py
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Digital Theatre API"
    DEBUG_MODE: bool = True
    API_V1_STR: str = "/api/v1"
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./digital_theatre.db"
    
    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()