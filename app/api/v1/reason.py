from fastapi import APIRouter
from app.models.reason import ReasonRequest, ReasonResponse,ReasonResponseStatus
from app.services.openrouter import call_openrouter

router = APIRouter()

@router.get("/", response_model=str)
async def welcome():
    return "Welcome to Thinkfast, make a POST call at /reason to get started"


@router.post("/reason", response_model=ReasonResponse)
async def reason(request: ReasonRequest):
    
    result = call_openrouter(request.api_key, request.model, request.messages)

    return ReasonResponse(error="0",reasoning="",response=result,status=ReasonResponseStatus.completed)
