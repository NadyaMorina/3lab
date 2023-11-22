from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.summarizer import Summarizer, SummarizerParams

root_router = APIRouter()


class SummarizeRequest(BaseModel):
    text: str
    params: SummarizerParams = SummarizerParams()


class SummarizeResponse(BaseModel):
    summary: str


@root_router.post('/text-summary')
def summarize_text(request: SummarizeRequest, summarizer: Annotated[Summarizer, Depends()]) -> SummarizeResponse:
    summary = summarizer.summarize(request.text, request.params)
    return SummarizeResponse(summary=summary)
