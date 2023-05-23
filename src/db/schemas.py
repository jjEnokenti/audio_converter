import uuid

from fastapi import File
from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    """Схема для создания пользователя."""
    username: str


class UserCreateResponse(BaseModel):
    user_id: uuid.UUID
    access_token: uuid.UUID


class AudioResponse(BaseModel):
    """Схема для скачивания аудио."""
    download_url: str
