from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

class Message(BaseModel):
    role: str = Field(..., description="Role of the message sender")
    content: str = Field(..., description="Content of the message")

class ReasonRequest(BaseModel):
    api_key: str = Field(..., description="User's OpenRouter API key")
    model: str = Field(..., description="OpenRouter model name")
    messages: List[Message] = Field(..., description="Conversation messages")

class ReasonResponse(BaseModel):
    result: str

app = FastAPI()

@app.post("/reason", response_model=ReasonResponse)
async def reason(request: ReasonRequest):
    return ReasonResponse(result="This will be end result after fetching from OpenRouter")
