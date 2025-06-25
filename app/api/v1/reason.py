from fastapi import APIRouter
from app.models.reason import ReasonRequest, ReasonResponse
from app.services.openrouter import fetch_reason_from_openrouter

router = APIRouter()

@router.get("/", response_model=ReasonResponse)
async def welcome():
    return ReasonResponse(result="Welcome from ThinkFast!, POST properly to start using the API")

@router.post("/reason", response_model=ReasonResponse)
async def reason(request: ReasonRequest):
    result = fetch_reason_from_openrouter(request.api_key, request.model, request.messages)
    return ReasonResponse(result=result)
