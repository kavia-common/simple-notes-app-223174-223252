from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List, Optional


@dataclass
class NoteRecord:
    """Internal storage representation for a note."""
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime


class InMemoryNoteStore:
    """
    A simple in-memory store for Notes.
    Designed so it can be swapped later with a database-backed implementation.
    """

    def __init__(self) -> None:
        self._records: Dict[int, NoteRecord] = {}
        self._next_id: int = 1

    # PUBLIC_INTERFACE
    def list_notes(self) -> List[NoteRecord]:
        """Return all notes as a list."""
        return list(self._records.values())

    # PUBLIC_INTERFACE
    def create_note(self, title: str, content: str) -> NoteRecord:
        """Create a new note and return it."""
        now = datetime.now(timezone.utc)
        record = NoteRecord(
            id=self._next_id,
            title=title,
            content=content,
            created_at=now,
            updated_at=now,
        )
        self._records[self._next_id] = record
        self._next_id += 1
        return record

    # PUBLIC_INTERFACE
    def get_note(self, note_id: int) -> Optional[NoteRecord]:
        """Get a single note by id, or None if not found."""
        return self._records.get(note_id)

    # PUBLIC_INTERFACE
    def update_note(self, note_id: int, *, title: Optional[str] = None, content: Optional[str] = None) -> Optional[NoteRecord]:
        """Update an existing note's fields and return the updated record, or None if not found."""
        record = self._records.get(note_id)
        if record is None:
            return None
        if title is not None:
            record.title = title
        if content is not None:
            record.content = content
        record.updated_at = datetime.now(timezone.utc)
        self._records[note_id] = record
        return record

    # PUBLIC_INTERFACE
    def delete_note(self, note_id: int) -> bool:
        """Delete a note by id. Returns True if deleted, False if not found."""
        if note_id in self._records:
            del self._records[note_id]
            return True
        return False


# A module-level store instance for simplicity (can be replaced by dependency injection later)
store = InMemoryNoteStore()
