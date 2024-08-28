from typing import Optional

from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'Личные заметки'
    description: str = ('Сервис для хранения личных заметок.')
    database_url: str = 'postgresql+asyncpg://postgres:postgres@db:5432/postgres'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
