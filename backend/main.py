import logging

from fastapi import FastAPI

from app.routes.auth import router as auth_router

logger = logging.getLogger(__name__)
app = FastAPI(
    title="ApplyTrack API",
    description="Job application tracking system",
    version="1.0.0"
)
app.include_router(auth_router)


@app.get("/")
def test_route():
    return {"message": "ApplyTrack backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}