"""In-memory storage for tasks."""

import uuid
from datetime import datetime
from typing import List, Optional
from app.models import Task, TaskCreate, StatusEnum


# In-memory task storage
tasks_db: List[Task] = []


def create_task(task_create: TaskCreate) -> Task:
    """Create a new task and store it."""
    task = Task(
        id=str(uuid.uuid4()),
        title=task_create.title,
        description=task_create.description,
        status=StatusEnum.pending,  # Always pending on creation
        created_at=datetime.utcnow(),
    )
    tasks_db.append(task)
    return task


def get_task(task_id: str) -> Optional[Task]:
    """Get a task by ID."""
    for task in tasks_db:
        if task.id == task_id:
            return task
    return None


def list_tasks() -> List[Task]:
    """List all tasks."""
    return tasks_db.copy()


def update_task(task_id: str, status: StatusEnum) -> Optional[Task]:
    """Update a task's status."""
    task = get_task(task_id)
    if task:
        task.status = status
        return task
    return None


def delete_task(task_id: str) -> bool:
    """Delete a task by ID."""
    global tasks_db
    original_length = len(tasks_db)
    tasks_db = [task for task in tasks_db if task.id != task_id]
    return len(tasks_db) < original_length


def clear_tasks() -> None:
    """Clear all tasks (for testing)."""
    global tasks_db
    tasks_db = []
