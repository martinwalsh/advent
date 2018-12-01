FROM python:3.7.1-alpine3.8

ENV PIPENV_VERSION 2018.10.13
RUN pip install pipenv==${PIPENV_VERSION}
WORKDIR /app

COPY Pipfile* /app/
RUN pipenv install --dev  --system --deploy
