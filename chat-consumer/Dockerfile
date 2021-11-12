# syntax=docker/dockerfile:1

FROM python:3.9.7-slim-buster

WORKDIR /chat-consumer

COPY /chat-consumer/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY /chat-consumer/ .

CMD ["python", "src/chat-consumer.py"]