from typing import Optional

from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'Личные заметки'
    description: str = ('Сервис для хранения личных заметок.')
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    model_config = SettingsConfigDict(env_file='.env')
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None


settings = Settings()
