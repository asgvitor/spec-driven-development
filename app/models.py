"""Pydantic models for Task Manager API."""

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class StatusEnum(str, Enum):
    """Valid task status values."""
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskCreate(BaseModel):
    """Model for creating a new task."""
    title: str = Field(..., min_length=1, description="Task title (required, non-empty)")
    description: Optional[str] = Field(None, description="Task description (optional)")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Buy groceries",
                "description": "Milk, bread, eggs"
            }
        }


class TaskUpdate(BaseModel):
    """Model for updating a task."""
    status: StatusEnum = Field(..., description="Task status (pending, in_progress, done)")

    class Config:
        json_schema_extra = {
            "example": {
                "status": "in_progress"
            }
        }


class Task(BaseModel):
    """Complete task model."""
    id: str = Field(..., description="Unique task identifier (UUID)")
    title: str = Field(..., description="Task title")
    description: Optional[str] = Field(None, description="Task description")
    status: StatusEnum = Field(default=StatusEnum.pending, description="Task status")
    created_at: datetime = Field(..., description="Task creation timestamp")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "title": "Buy groceries",
                "description": "Milk, bread, eggs",
                "status": "pending",
                "created_at": "2026-04-29T12:00:00"
            }
        }


class ErrorResponse(BaseModel):
    """Standard error response model."""
    error: str = Field(..., description="Error message")
    code: str = Field(..., description="Error code identifier")

    class Config:
        json_schema_extra = {
            "example": {
                "error": "Task not found",
                "code": "NOT_FOUND"
            }
        }
