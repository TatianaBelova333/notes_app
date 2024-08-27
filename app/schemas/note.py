from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.core.constants import NOTE_MAX_LEN, STR_MIN_VAL
from app.services.spelling_check import correct_typos


class PriorityEnum(str, Enum):
    '''Enum class for the priority levels of notes.'''
    HIGH = 'Важное'
    MEDIUM = 'Среднее'
    LOW = 'Неважное'


class TagEnum(str, Enum):
    '''Enum Class for note tags.'''
    WORK = 'Работа'
    SPORT = 'Спорт'
    STUDY = 'Учеба'
    SHOPPING = 'Покупки'
    PLEASURE = 'Развлечение'


class NoteBase(BaseModel):
    '''Base schema for Note model.'''
    model_config = ConfigDict(
        str_min_length=STR_MIN_VAL,
        str_strip_whitespace=True,
    )

    content: Optional[str] = Field(None, max_length=NOTE_MAX_LEN)
    priority: Optional[PriorityEnum] = PriorityEnum.LOW
    tag: Optional[TagEnum] = None


class NoteUpdate(NoteBase, extra='forbid'):
    '''Schema for updating a note.'''

    @field_validator('content')
    @correct_typos
    def check_for_typos(cls, content: str):
        if content is None:
            raise ValueError('Content cannot be null.')
        return content


class NoteCreate(NoteBase, extra='forbid'):
    '''Schema for creating a new Note.'''
    content: str = Field(..., max_length=NOTE_MAX_LEN)

    @field_validator('content')
    @correct_typos
    def check_for_typos(cls, content: str):
        return content


class NoteDB(NoteBase):
    """Schema for retrieving Note instances."""

    # model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    user_id: int
    title: str
