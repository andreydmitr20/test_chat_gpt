import asyncio

import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import as_declarative, sessionmaker

from .config import config
from .log import d, log

SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://"
    + config.db_user
    + ":"
    + config.db_pass
    + "@"
    + config.db_host
    + ":"
    + config.db_port
    + "/"
    + config.db_name
)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=config.db_echo)
async_db_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db_session() -> AsyncSession:
    async with async_db_session() as db_session:
        yield db_session
