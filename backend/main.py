import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import engine

logger = logging.getLogger(__name__)
app = FastAPI(
    title="ApplyTrack API",
    description="Job application tracking system",
    version="1.0.0"
)

@app.get("/")
def test_route():
    return {"message": "Job tracker API is working"}