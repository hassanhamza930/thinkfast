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
    

    tempReqParamsForReasing:ReasonRequest = ReasonRequest(
        api_key=request.api_key,
        messages=
         [
            Message(
                role=MessageRole.system,
                content="You are a helpful reasoning assistant, your goal is to come up with unique, never seen before ideas and approaches," \
                "you give extremely detailed planning on how to answer user based on whatever they ask or write, You will periodically question yourself with something like," \
                "i think this is good, but wait this might be wrong i should check. For Example, 'Ok this looks good but wait i should also think about another approach.' etc" \
                " No Matter what user writes your whole goal is to think about how to answer and you should only explain how to potentially answer user's question."
                )
        ]+
        request.messages,
        model="google/gemini-2.5-flash-lite-preview-06-17"
    )
    

    try:
        responses: tuple[ReasonResponse, ...] = await asyncio.gather(
            call_openrouter(params=tempReqParamsForReasing),
            call_openrouter(params=tempReqParamsForReasing ),
            call_openrouter(params=tempReqParamsForReasing)
        )

        combined_reasoning = "\n\n\n".join([res.response for res in responses])

        conciledResult:ReasonResponse=await call_openrouter(params=ReasonRequest(
            api_key=request.api_key,
            messages= request.messages + [
                Message(
                    role=MessageRole.assistant,
                    content="OK Now i will extensively think about it: "+combined_reasoning
                ),
                Message(
                    role=MessageRole.user,
                    content="Now briefly Concile all of your thoughts & answer my query"
                )
            ],
            model=request.model
        ))

        conciledResult.reasoning=combined_reasoning
        
        return conciledResult
    except Exception as e:

        return ReasonResponse(
            error=str(e),
            response="Query Failed",
            reasoning="No Reasoning Tokens",
            status=ReasonResponseStatus.failed
    )
