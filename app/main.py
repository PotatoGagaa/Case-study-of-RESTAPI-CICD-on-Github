from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task Management API",
    version="1.0.0",
    description="A small REST API used for a GitHub Actions CI/CD case study.",
)

# In-memory storage keeps this learning project simple.
# Data resets whenever the application process restarts.
_tasks: dict[int, dict] = {}
_next_id = 1

# This is a demo-only token. Never use a real production token here.
TEST_API_TOKEN = "demo-test-token"
# Change to use an environment variable in production code.
#TEST_API_TOKEN = os.environ["TEST_API_TOKEN"]

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)


def require_test_token(
    x_api_token: Annotated[str | None, Header()] = None,
) -> None:
    if x_api_token != TEST_API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API token",
        )


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tasks", dependencies=[Depends(require_test_token)])
def list_tasks() -> list[dict]:
    return list(_tasks.values())


@app.post(
    "/tasks",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_test_token)],
)
def create_task(task: TaskCreate) -> dict:
    global _next_id
    record = {
        "id": _next_id,
        "title": task.title,
        "description": task.description,
    }
    _tasks[_next_id] = record
    _next_id += 1
    return record


@app.get("/tasks/{task_id}", dependencies=[Depends(require_test_token)])
def get_task(task_id: int) -> dict:
    task = _tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_test_token)],
)
def delete_task(task_id: int) -> None:
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del _tasks[task_id]
