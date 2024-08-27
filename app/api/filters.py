from datetime import datetime
from typing import Optional

from fastapi import Query
from fastapi_filter.contrib.sqlalchemy import Filter

from pydantic import Field

from app.models import Note
from app.schemas import PriorityEnum, TagEnum


class NoteFilter(Filter):
    content__ilike: Optional[str] = None
    created_at__gte: Optional[datetime] = None
    tag__in: Optional[TagEnum] = None
    priority__in: Optional[PriorityEnum] = None

    class Constants(Filter.Constants):
        model = Note
        search_model_fields = ('content',)

    class Config:
        populate_by_field_name = True
