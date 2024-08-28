from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.constants import NOTE_MAX_LEN, NOTE_TITLE_LEN
from app.core.db import Base
from app.models.enums import PriorityEnum, TagEnum


class Note(Base):
    """DB model for user's notes."""
    content: Mapped[str] = mapped_column(String(NOTE_MAX_LEN), nullable=False)
    created_at: Mapped[Optional[datetime]] = mapped_column(
        index=True, server_default=func.now())
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        index=True, onupdate=func.now())
    priority: Mapped[PriorityEnum] = mapped_column(
        default=PriorityEnum.LOW, values_callable=lambda obj: [e.value for e in obj])
    tag: Mapped[TagEnum] = mapped_column(
        default=TagEnum.MISCELLANEOUS, values_callable=lambda obj: [e.value for e in obj])
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user: Mapped['User'] = relationship(back_populates='notes')

    @hybrid_property
    def title(self) -> str:
        return self.content[:NOTE_TITLE_LEN]
