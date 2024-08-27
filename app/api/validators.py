from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.note import get_note_by_id_and_user
from app.models import User
from app.schemas import NoteDB


async def check_note_exists(note_id: int,
                            session: AsyncSession,
                            user: User) -> NoteDB:
    '''
    Return a Note instance by note id and current user id.
    Raise a 404 Not Found HTTPException, otherwise.

    '''
    note = await get_note_by_id_and_user(
        note_id=note_id, session=session, user=user
    )

    if note is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='The note is not found.',
        )
    return note
