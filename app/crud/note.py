from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.filters import NoteFilter
from app.models import Note, User
from app.schemas import NoteCreate, NoteDB, NoteUpdate


async def create_note(new_note: NoteCreate,
                      session: AsyncSession,
                      user: User) -> Note:
    '''Create and return a new note.'''
    new_note_data = new_note.model_dump()
    new_note_data['user_id'] = user.id

    db_note = Note(**new_note_data)
    session.add(db_note)

    await session.commit()
    await session.refresh(db_note)

    return db_note


async def read_all_user_notes_from_db(
        note_filter: NoteFilter,
        user: User,
        session: AsyncSession) -> list[NoteDB]:
    '''
    Return a list of the current user's notes ordered by
    updated_at and created_at fields in descending order.

    '''
    query_filter = note_filter.filter(
        select(Note).where(
            Note.user_id == user.id
        ).order_by(
            desc(Note.updated_at),
            desc(Note.created_at),
        ))
    db_notes = await session.execute(query_filter)
    return db_notes.scalars().all()


async def get_note_by_id_and_user(note_id: int,
                                  session: AsyncSession,
                                  user: User) -> Optional[NoteDB]:
    '''
    Retrieve and return a note by note id and current user id.
    Return None if not found.

    '''
    db_note = await session.execute(
        select(Note).where(
            Note.id == note_id,
            Note.user_id == user.id,
        )
    )
    db_note = db_note.scalars().first()
    return db_note


async def update_note(db_note: NoteDB,
                      note_in: NoteUpdate,
                      session: AsyncSession) -> NoteDB:

    obj_data = jsonable_encoder(db_note)

    updated_data = note_in.model_dump(exclude_unset=True)

    for field in obj_data:
        if field in updated_data:
            setattr(db_note, field, updated_data[field])

    session.add(db_note)
    await session.commit()
    await session.refresh(db_note)

    return db_note


"""
async def read_all_user_notes_from_db(user: User,
                                      session: AsyncSession) -> list[NoteDB]:
    '''
    Return a list of the current user's notes ordered by
    updated_at and created_at fields in descending order.

    '''
    query_filter = product_filter.filter(select(Product))
    db_notes = await session.execute(
        select(Note).where(
            Note.user_id == user.id
        ).order_by(
            desc(Note.updated_at),
            desc(Note.created_at),
        )
    )
    return db_notes.scalars().all()
"""