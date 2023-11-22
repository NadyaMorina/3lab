import logging
from abc import abstractmethod, ABC
from typing import Protocol

from pydantic import BaseModel
from transformers import pipeline, Pipeline

# https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.SummarizationPipeline
# https://huggingface.co/docs/transformers/en/main_classes/text_generation#transformers.generation.GenerationMixin.generate


class SummarizerParams(BaseModel):
    min_length: int = 30
    max_length: int = 130
    do_sample: bool = False


class Summarizer(ABC):
    @abstractmethod
    def summarize(self, text: str, params: SummarizerParams) -> str:
        ...


class TransformersSummarizer(Summarizer):
    @classmethod
    def from_model_name(cls, model_name: str):
        logging.info('start loading model %s', model_name)
        summarizer = cls(
            pipeline(
                "summarization",
                model=model_name,
            )
        )
        logging.info('model %s is loaded', model_name)
        return summarizer

    def __init__(self, ready_pipeline: Pipeline):
        self._pipeline = ready_pipeline

    def summarize(self, text: str, params: SummarizerParams) -> str:
        result = self._pipeline(text, **params.model_dump())
        return result[0]['summary_text']

