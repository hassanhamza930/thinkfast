from typing import List
from pydantic import BaseModel, Field
from app.models.message import Message
from enum import Enum

class ReasonResponseStatus(str,Enum):
    processing= "processing"
    completed="completed"
    failed="failed"


class ReasonRequest(BaseModel):
    api_key: str = Field(..., description="User's OpenRouter API key")
    model: str = Field(..., description="OpenRouter model value")
    messages: List[Message] = Field(..., description="Messages Array with ")

class ReasonResponse(BaseModel):
    reasoning:str = Field(..., description="Reasoning Tokens")
    response: str = Field(..., description="Actual Response")
    error:str = Field(..., description="Error During Reasoning Request")
    status:ReasonResponseStatus = Field(..., description="Status of Reasoning Request")
