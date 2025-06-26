# Placeholder for OpenRouter integration logic

from typing import List, cast
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam
from app.models.reason import ReasonRequest,ReasonResponse,ReasonResponseStatus

async def call_openrouter(params:ReasonRequest) -> ReasonResponse:

    client = AsyncOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=params.api_key,
    )

    messagesToPass: List[ChatCompletionMessageParam] = [
        cast(ChatCompletionMessageParam, {"role": m.role, "content": m.content})
        for m in params.messages
    ]

    completion = await client.chat.completions.create(
        model=params.model,
        messages=messagesToPass
    )
    response_content = completion.choices[0].message.content or ""
    return ReasonResponse(
        reasoning="",
        response=response_content,
        status=ReasonResponseStatus.completed
    )
    





