# Placeholder for OpenRouter integration logic

from typing import List, cast
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from app.models.reason import ReasonRequest,ReasonResponse,ReasonResponseStatus

def call_openrouter(params:ReasonRequest) -> ReasonResponse:

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=params.api_key,
    )

    messagesToPass: List[ChatCompletionMessageParam] = [
        cast(ChatCompletionMessageParam, {"role": m.role, "content": m.content})
        for m in params.messages
    ]

    try:
        completion = client.chat.completions.create(
            model=params.model,
            messages=messagesToPass
        )
        response_content = completion.choices[0].message.content or ""
        return ReasonResponse(
            reasoning="OpenRouter call successful",
            response=response_content,
            error="",
            status=ReasonResponseStatus.completed
        )
    except Exception as e:
        return ReasonResponse(
            reasoning="",
            response="",
            error=str(e),
            status=ReasonResponseStatus.failed
        )
