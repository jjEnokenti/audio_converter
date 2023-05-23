import uuid

from sqlalchemy import select, and_

from src.db import User, session, Audio


async def get_user(
        user_id: uuid.UUID,
        access_token: uuid.UUID) -> User | None:
    """Отдает объект пользователя из базы."""

    statement = select(User).where(
        and_(
            User.id == user_id,
            User.access_token == access_token
        )
    )
    result = await session.execute(statement)
    user = result.scalar_one_or_none()

    return user


async def get_record(
        audio_id: uuid.UUID,
        user_id: uuid.UUID) -> Audio | None:

    """Отдает объект аудио из базы."""
    statement = select(Audio).where(
        and_(
            Audio.id == audio_id,
            Audio.user_id == user_id
        )
    )
    result = await session.execute(statement)
    record = result.scalar_one_or_none()

    return record


async def create_user(username: str) -> User:
    """Создает пользователя."""
    user = User(**{'username': username})
    session.add(user)
    return user


async def add_audio(
        user_id: uuid.UUID,
        path_save: str,
        filename: str) -> Audio:
    """Создает аудио."""
    audio = Audio(**{
        'user_id': user_id,
        'path_to_file': path_save,
        'filename': filename
    })
    session.add(audio)

    return audio
