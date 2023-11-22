import logging

from fastapi import FastAPI

from app.routes import root_router
from app.summarizer import Summarizer, TransformersSummarizer


def setup_dependencies(app: FastAPI) -> None:
    summarizer = TransformersSummarizer.from_model_name('facebook/bart-large-cnn')
    app.dependency_overrides[Summarizer] = lambda: summarizer


def create_app() -> FastAPI:
    logging.basicConfig(level=logging.INFO)
    app = FastAPI()
    app.include_router(root_router)
    setup_dependencies(app)
    return app
