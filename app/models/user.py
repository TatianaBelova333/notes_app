from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, relationship

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    notes: Mapped['Note'] = relationship(back_populates='user',
                                         lazy='selectin',
                                         cascade='delete',)
