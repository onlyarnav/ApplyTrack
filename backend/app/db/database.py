from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, DeclarativeBase

from ..core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass