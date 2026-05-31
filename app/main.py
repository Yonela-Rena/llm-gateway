from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.models.response_model import ChatResponse
from app.services.ai_service import generate_response

app = FastAPI()


class PromptRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "LLM Gateway is running!"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: PromptRequest):

    try:
        if not request.message.strip():
            raise HTTPException(
                status_code=400,
                detail="Message cannot be empty"
            )

        response = generate_response(request.message)

        return {
            "response": response,
            "status": "success"
        }

    except Exception as e:
        return {
            "response": str(e),
            "status": "failed"
        }