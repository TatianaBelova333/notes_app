from datetime import datetime
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from app.models import Note


class NoteFilter(Filter):
    '''Filterset for filtering current user's notes.'''
    content__ilike: Optional[str] = None
    created_at__gte: Optional[datetime] = None
    created_at__lte: Optional[datetime] = None

    class Constants(Filter.Constants):
        model = Note
        search_model_fields = ('content',)

    class Config:
        populate_by_field_name = True
