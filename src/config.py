import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DATABASE_URL = (f'postgresql+asyncpg://'
                f'{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')

BASE_DIR = Path(__file__).resolve().parent.parent
