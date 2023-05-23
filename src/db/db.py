from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base

from src.config import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
    future=True
)

async_session = AsyncSession(
    bind=async_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

Base = declarative_base()
