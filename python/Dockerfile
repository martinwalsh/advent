FROM python:3.9-alpine3.12

RUN pip install --upgrade pip setuptools wheel && \
      pip install pipenv
WORKDIR /app

COPY Pipfile* /app/
RUN pipenv install --dev --system --deploy
