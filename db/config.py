from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.settings import Settings
from fastapi import Security
from utils.auth import auth as ai_auth
from fastapi.security import HTTPAuthorizationCredentials

settings = Settings()

DATABASE_URL = settings.database_url
engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session():
    try:
        async with async_session() as session:
            async with session.begin():
                yield session
    finally:
        await session.close()


# auth dependencies
def auth_required(
    auth: HTTPAuthorizationCredentials = Security(ai_auth.security),
) -> int:
    payload = ai_auth.decode_token(auth.credentials)
    return payload["user_id"]
