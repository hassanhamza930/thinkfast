from fastapi import APIRouter
from app.models.reason import ReasonRequest, ReasonResponse,ReasonResponseStatus
from app.services.openrouter import call_openrouter
from app.models.message import Message,MessageRole
import asyncio

router = APIRouter()

@router.get("/", response_model=str)
async def welcome():
    return "Welcome to Thinkfast, make a POST call at /reason to get started"


@router.post("/reason", response_model=ReasonResponse)
async def reason(request: ReasonRequest):
    

    tempReqParams:ReasonRequest = ReasonRequest(
        api_key="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",
        messages=
         [
            Message(
                role=MessageRole.system,
                content="You are a helpful planning & research assistant, your goal is to come up with unique, never seen before, extremely detailed planning on how to answer user based on whatever they ask or write, You will periodically question yourself with something like, i think this is good, but wait this might be wrong i should check. No Matter what user writes your whole goal is to think about how to answer and you should only explain how to potentially answer user's question."
                )
        ]+
        request.messages,
        model="google/gemini-2.5-flash-lite-preview-06-17"
    )
    

    try:
        responses: tuple[ReasonResponse, ...] = await asyncio.gather(
            call_openrouter(params=tempReqParams),
            call_openrouter(params=tempReqParams),
            call_openrouter(params=tempReqParams)
        )

        combined_reasoning = "\n\n\n".join([res.response+"               pass completed           " for res in responses])

        return ReasonResponse(
            error="",
            reasoning=combined_reasoning,
            response="",
            status=ReasonResponseStatus.completed
        )
    except Exception as e:

        return ReasonResponse(
            error=str(e),
            response="Query Failed",
            reasoning="No Reasoning Tokens",
            status=ReasonResponseStatus.failed
    )
