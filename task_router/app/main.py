from fastapi import FastAPI
from pydantic import BaseModel
from task_router.event_producer import route_task_to_agent

app = FastAPI()

class TaskRequest(BaseModel):
    user_id: str
    instruction: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/v1/task/submit")
def submit_user_task(request: TaskRequest):
    status = route_task_to_agent(request.user_id, request.instruction)
    return status
