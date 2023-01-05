FROM python:3.11-alpine

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.3.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY app/poetry.lock app/pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY app /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]