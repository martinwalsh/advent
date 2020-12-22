FROM python:3.9.1-slim-buster

RUN pip install --upgrade pip setuptools wheel && \
      pip install pipenv
WORKDIR /app

COPY Pipfile* /app/
RUN pipenv install --dev --system --deploy
