from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType

from app.core.constants import NOTE_TITLE_LEN, PRIORITY_MAX_VAL, TAG_MAX_VAL
from app.core.db import Base
from app.schemas import PriorityEnum, TagEnum


class Note(Base):
    """DB model for user's notes."""
    content = Column(Text, nullable=False)
    created_at = Column(
        DateTime,
        nullable=False,
        index=True,
        server_default=func.now(),
    )
    updated_at = Column(
        DateTime,
        index=True,
        onupdate=func.now(),
    )
    priority = Column(ChoiceType(PriorityEnum, impl=String(PRIORITY_MAX_VAL)))
    tag = Column(ChoiceType(TagEnum, impl=String(TAG_MAX_VAL)))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='notes')

    @hybrid_property
    def title(self) -> str:
        return self.content[:NOTE_TITLE_LEN]
