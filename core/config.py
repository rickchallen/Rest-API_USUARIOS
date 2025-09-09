import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Carrega as configurações do ambiente ou do arquivo .env.
    """
    MOCK_USERS_FILE_PATH: str = "mock-users.json"
    API_TITLE: str = "API de Usuários"
    API_VERSION: str = "1.0.0"
    LOG_FILE_PATH: str = "app.log"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()