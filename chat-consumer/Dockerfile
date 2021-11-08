# syntax=docker/dockerfile:1

FROM python:3.9.7-slim-buster

WORKDIR /chat-consumer

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "src.chat-consumer.py"]