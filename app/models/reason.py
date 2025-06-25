from typing import List
from pydantic import BaseModel, Field
from app.models.message import Message

class ReasonRequest(BaseModel):
    api_key: str = Field(..., description="User's OpenRouter API key")
    model: str = Field(..., description="OpenRouter model name")
    messages: List[Message] = Field(..., description="Conversation messages")

class ReasonResponse(BaseModel):
    result: str
