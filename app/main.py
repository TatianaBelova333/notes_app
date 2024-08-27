import logging

from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
from app.core.constants import LOGGING_FILE, LOGGING_FILE_MODE, LOGGING_FORMAT

app = FastAPI(title=settings.app_name)

app.include_router(main_router)

logging.basicConfig(
    level=logging.INFO,
    filename=LOGGING_FILE,
    filemode=LOGGING_FILE_MODE,
    format=LOGGING_FORMAT,
)
logger = logging.getLogger(__name__)
