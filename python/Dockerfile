FROM python:3.9.1-slim-buster

RUN pip install --upgrade pip setuptools wheel && \
      pip install pipenv && \
      apt-get update && \
      apt-get install -y less && \
      apt-get clean && \
      rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY Pipfile* /app/
RUN pipenv install --dev --system --deploy
