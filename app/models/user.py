from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    notes = relationship(
        'Note',
        back_populates='user',
        lazy='selectin',
        cascade='delete',
    )
