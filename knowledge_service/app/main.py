from fastapi import FastAPI
from pydantic import BaseModel
from knowledge_service.app.services.kg_processor import execute_knowledge_query
from knowledge_service.app.services.llm_integrator import generate_contextual_answer

app = FastAPI()

class KnowledgeRequest(BaseModel):
    user_id: str
    question: str
    tag: str

@app.post("/api/v1/knowledge/query")
def process_knowledge_query(request: KnowledgeRequest):
    kg_results = execute_knowledge_query(request.user_id, request.tag)
    final_answer = generate_contextual_answer(request.question, kg_results)
    return {"status": "success", "answer": final_answer, "sources": kg_results}
