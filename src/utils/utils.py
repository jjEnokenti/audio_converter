import uuid
from typing import BinaryIO

import pydub  # type: ignore

from src.config import BASE_DIR


def converting_wav_to_mp3(wav_file: BinaryIO):
    filename = uuid.uuid4()
    path_save = f'{BASE_DIR}/audio_files/{filename}.mp3'

    sound: pydub.AudioSegment = pydub.AudioSegment.from_wav(wav_file)
    sound.export(path_save, format='mp3')

    return path_save


if __name__ == '__main__':
    pass
