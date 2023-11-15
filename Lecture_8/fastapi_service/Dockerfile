FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.2.0 \
    POETRY_HOME=/opt/poetry

RUN curl -sSL https://install.python-poetry.org | python - --version 1.2.0 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml /app/

RUN poetry lock --no-update && poetry install --no-root --no-dev

COPY service service
