FROM python:3.10-slim

RUN apt update && apt upgrade
RUN apt-get install -y ffmpeg

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ../requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

ENV PYTHONPATH '/app'