# syntax=docker/dockerfile:1
# GERENCIADOR DE CONFIGURAÇÃO TERRAFORM, VALIDAR DEPOIS ***

ARG APP_NAME=chat_consumer
ARG APP_PATH=/opt/$APP_NAME

#STAGING
FROM python:latest as staging
ARG APP_NAME
ARG APP_PATH

ENV \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONFAULTHANDLER=1
ENV \
  POETRY_HOME="/opt/poetry" \
  POETRY_VIRTUALENVS_IN_PROJECT=true \
  POETRY_NO_INTERACTION=1

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR $APP_PATH
COPY ./chat_consumer/ .

#DEVELOPMENT
FROM staging as development
ARG APP_PATH

WORKDIR $APP_PATH

RUN poetry install

ENTRYPOINT ["poetry", "run"]
CMD ["python", "src/chat_consumer.py"]
