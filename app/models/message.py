from enum import Enum
from pydantic import BaseModel, Field

class MessageRole(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"

class Message(BaseModel):
    role: MessageRole = Field(..., description="Role of the message sender")
    content: str = Field(..., description="Content of the message")


