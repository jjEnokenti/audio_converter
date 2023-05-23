import uuid
from typing import BinaryIO

from fastapi import HTTPException, UploadFile
from sqlalchemy.exc import DBAPIError
from starlette import status

from src.db import session, Audio, crud, User
from src.utils.utils import converting_wav_to_mp3


async def create_user(username: str) -> User:
    """Сервис слой для создания пользователя."""

    try:
        async with session.begin():
            user: User = await crud.create_user(username)
    except DBAPIError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"error message: {error.args[0]}"
        )
    return user


async def download_audio(
        audio_id: uuid.UUID,
        user_id: uuid.UUID) -> Audio:
    """Сервисный слой для скачивания аудио."""

    try:
        async with session.begin():
            audio = await crud.get_record(audio_id=audio_id, user_id=user_id)
            if not audio:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Audio not found"
                )
    except DBAPIError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"error message: {error.args[0]}"
        )
    return audio


async def add_audio(
        user_id: uuid.UUID,
        access_token: uuid.UUID,
        audio_file: BinaryIO,
        filename: str | None) -> Audio:
    """Сервисный слой для добавления аудио."""

    path_save = converting_wav_to_mp3(audio_file)
    if filename:
        filename = filename.split('.')[0]
    else:
        filename = 'unknown'

    try:
        async with session.begin():
            if not await crud.get_user(user_id, access_token):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid user_id or access_token"
                )

            audio: Audio = await crud.add_audio(
                user_id=user_id,
                path_save=path_save,
                filename=filename
            )
    except DBAPIError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"error message: {error.args[0]}"
        )

    return audio
