FROM python:3.11.0-alpine

ARG PIPENV_VERS=2022.11.30
RUN pip install pipenv==${PIPENV_VERS}
WORKDIR /app

COPY Pipfile* /app/
RUN pipenv install --dev  --system --deploy
