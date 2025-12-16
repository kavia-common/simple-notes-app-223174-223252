from typing import List

from fastapi import APIRouter, HTTPException, Path, status

from ..models.schemas import Note, NoteCreate, NoteUpdate
from ..storage.memory import store

router = APIRouter()


@router.get(
    "",
    response_model=List[Note],
    status_code=status.HTTP_200_OK,
    summary="List notes",
    description="Return a list of all notes.",
    responses={
        200: {"description": "List of notes returned successfully."},
    },
)
# PUBLIC_INTERFACE
def list_notes() -> List[Note]:
    """List all notes."""
    return [Note(**record.__dict__) for record in store.list_notes()]


@router.post(
    "",
    response_model=Note,
    status_code=status.HTTP_201_CREATED,
    summary="Create note",
    description="Create a new note with title and content.",
    responses={
        201: {"description": "Note created successfully."},
        422: {"description": "Validation error."},
    },
)
# PUBLIC_INTERFACE
def create_note(payload: NoteCreate) -> Note:
    """Create a new note."""
    record = store.create_note(title=payload.title, content=payload.content)
    return Note(**record.__dict__)


@router.get(
    "/{note_id}",
    response_model=Note,
    status_code=status.HTTP_200_OK,
    summary="Get note",
    description="Get a note by ID.",
    responses={
        200: {"description": "Note returned successfully."},
        404: {"description": "Note not found."},
    },
)
# PUBLIC_INTERFACE
def get_note(
    note_id: int = Path(..., ge=1, description="ID of the note to retrieve"),
) -> Note:
    """Get a single note by id."""
    record = store.get_note(note_id)
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return Note(**record.__dict__)


@router.put(
    "/{note_id}",
    response_model=Note,
    status_code=status.HTTP_200_OK,
    summary="Update note",
    description="Update a note's title and/or content by ID.",
    responses={
        200: {"description": "Note updated successfully."},
        404: {"description": "Note not found."},
        422: {"description": "Validation error."},
    },
)
# PUBLIC_INTERFACE
def update_note(
    payload: NoteUpdate,
    note_id: int = Path(..., ge=1, description="ID of the note to update"),
) -> Note:
    """Update a note by id."""
    if payload.title is None and payload.content is None:
        # nothing to update; treat as validation error
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="No fields provided to update")
    record = store.update_note(note_id, title=payload.title, content=payload.content)
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return Note(**record.__dict__)


@router.delete(
    "/{note_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete note",
    description="Delete a note by ID.",
    responses={
        204: {"description": "Note deleted successfully."},
        404: {"description": "Note not found."},
    },
)
# PUBLIC_INTERFACE
def delete_note(
    note_id: int = Path(..., ge=1, description="ID of the note to delete"),
) -> None:
    """Delete a note by id."""
    deleted = store.delete_note(note_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    # 204 No Content response
    return None
