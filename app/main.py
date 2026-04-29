"""Task Manager API - FastAPI application entry point."""

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic_core import ValidationError as PydanticValidationError
from typing import List

from app.models import ErrorResponse, Task, TaskCreate, TaskUpdate
from app import storage

# Initialize FastAPI app
app = FastAPI(
    title="Task Manager API",
    description="Simple task management API with in-memory storage",
    version="0.1.0",
)

# Add CORS middleware for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception handlers for error standardization

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """Handle Pydantic validation errors."""
    # Extract first validation error for simplicity
    errors = exc.errors()
    if errors:
        first_error = errors[0]
        error_msg = f"{first_error['msg']} in {first_error['loc'][-1]}"
    else:
        error_msg = "Validation failed"
    
    error_response = ErrorResponse(
        error=error_msg,
        code="VALIDATION_ERROR"
    )
    return JSONResponse(
        status_code=422,
        content=error_response.model_dump()
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle general exceptions."""
    error_response = ErrorResponse(
        error=str(exc),
        code="INTERNAL_ERROR"
    )
    return JSONResponse(
        status_code=500,
        content=error_response.model_dump()
    )


# Endpoints

@app.get("/")
async def health_check() -> dict:
    """Health check endpoint - validates API is alive.
    
    Returns:
        HTTP 200 with {"status": "ok"}
    """
    return {"status": "ok"}


@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task_create: TaskCreate) -> Task:
    """Create a new task.
    
    Args:
        task_create: TaskCreate model with title and optional description
        
    Returns:
        Created Task with id, title, description, status=pending, created_at
        
    Raises:
        422: If validation fails (title empty or missing)
    """
    return storage.create_task(task_create)


@app.get("/tasks", response_model=List[Task])
async def list_tasks() -> List[Task]:
    """List all tasks.
    
    Returns:
        List of all tasks (empty array if no tasks exist)
    """
    return storage.list_tasks()


@app.patch("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, task_update: TaskUpdate) -> Task:
    """Update a task's status.
    
    Args:
        task_id: UUID of the task to update
        task_update: TaskUpdate model with new status
        
    Returns:
        Updated Task with new status
        
    Raises:
        404: If task not found
        422: If status is invalid (not in enum)
    """
    updated = storage.update_task(task_id, task_update.status)
    if updated is None:
        error_response = ErrorResponse(
            error="Task not found",
            code="NOT_FOUND"
        )
        raise HTTPException(
            status_code=404,
            detail=error_response.model_dump()
        )
    return updated


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
