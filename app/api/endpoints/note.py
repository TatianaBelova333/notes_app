from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.filters import NoteFilter
from app.api.validators import check_note_exists
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.note import create_note, update_note, read_all_user_notes_from_db
from app.models import User
from app.schemas.note import NoteCreate, NoteDB, NoteUpdate

router = APIRouter()


@router.post('/', response_model=NoteDB)
async def create_new_note(note: NoteCreate,
                          session: AsyncSession = Depends(get_async_session),
                          user: User = Depends(current_user)):
    '''Create and return a new note.'''

    new_note = await create_note(new_note=note,
                                 session=session,
                                 user=user)
    return new_note


@router.get('/',
            dependencies=[Depends(current_user)],
            response_model=list[NoteDB])
async def get_all_user_notes(
        note_filter: NoteFilter = FilterDepends(NoteFilter),
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    '''Return a lis of the current user's notes.'''

    all_user_notes = await read_all_user_notes_from_db(
        note_filter=note_filter,
        session=session,
        user=user
    )
    return all_user_notes


@router.patch('/{note_id}',
              response_model=NoteDB,
              response_model_exclude_none=True)
async def partially_update_note(
        note_id: int,
        obj_in: NoteUpdate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)):
    '''Partially update a note.'''

    note = await check_note_exists(note_id=note_id, session=session, user=user)
    note = await update_note(note, obj_in, session)
    return note


@router.get('/{note_id}', response_model=NoteDB)
async def get_one_user_note(note_id: int,
                            session: AsyncSession = Depends(get_async_session),
                            user: User = Depends(current_user)):
    '''Return a note by id if the note belongs to the currect user.'''

    note = await check_note_exists(note_id=note_id, session=session, user=user)
    return note
