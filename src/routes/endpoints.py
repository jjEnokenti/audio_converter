import os
import uuid

from fastapi import FastAPI, File, UploadFile, Form, status
from fastapi.responses import FileResponse

from src.config import settings
from src.db import Audio
from src.db.schemas import UserCreateRequest, UserCreateResponse, AudioResponse
from src.services import service


def create_app() -> FastAPI:
    fastapi_app = FastAPI(
        title='Audio Converter',
        description='Конвертирует аудио файлы формата "wav" в формат "mp3"',
        version='0.1.0'
    )

    return fastapi_app


app = create_app()


@app.post(
    '/users/',
    description='Создание пользователя ',
    summary='создание пользователя',
    status_code=status.HTTP_201_CREATED,
    response_model=UserCreateResponse
)
async def create_user(request: UserCreateRequest) -> dict:
    user = await service.create_user(request.username)

    return {'user_id': user.id, 'access_token': user.access_token}


@app.post(
    '/audio/',
    description='Добавление аудиозаписи',
    summary='добавление аудиозаписи',
    status_code=status.HTTP_201_CREATED,
    response_model=AudioResponse
)
async def add_audio(
        user_id: uuid.UUID = Form(...),
        access_token: uuid.UUID = Form(...),
        audio_data: UploadFile = File(...)
):
    audio = await service.add_audio(
        user_id=user_id,
        access_token=access_token,
        audio_file=audio_data.file,
        filename=audio_data.filename
    )

    download_url = (f'/record?id={audio.id}&user={user_id}')

    return {'download_url': download_url}


@app.get(
    '/record/',
    description='Доступ к скачиванию записи',
    summary='доступ к записи',
    status_code=status.HTTP_200_OK,
)
async def download_audio(id: uuid.UUID, user: uuid.UUID):
    audio: Audio = await service.download_audio(audio_id=id, user_id=user)

    path_to_download = os.path.join(settings.BASE_DIR, audio.path_to_file)

    return FileResponse(
        path=path_to_download,
        filename=f'{audio.filename}.mp3'
    )
