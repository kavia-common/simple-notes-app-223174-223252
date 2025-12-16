from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NoteBase(BaseModel):
    """Base fields for a note."""

    title: str = Field(..., description="Short title of the note", min_length=1, max_length=200)
    content: str = Field(..., description="Content/body of the note", min_length=1)


class NoteCreate(NoteBase):
    """Schema for creating a new note."""
    pass


class NoteUpdate(BaseModel):
    """Schema for updating an existing note. All fields optional."""
    title: Optional[str] = Field(None, description="Updated title of the note", min_length=1, max_length=200)
    content: Optional[str] = Field(None, description="Updated content/body of the note", min_length=1)


class Note(NoteBase):
    """Schema returned for a note resource, including server-managed fields."""
    id: int = Field(..., description="Unique identifier")
    created_at: datetime = Field(..., description="Creation timestamp (UTC)")
    updated_at: datetime = Field(..., description="Last update timestamp (UTC)")

    class Config:
        from_attributes = True
