################################
# BASE
################################
FROM python:3.12.6-slim-bookworm as python-base

ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.0 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    VIRTUAL_ENV="/venv" \
    NODE_MAJOR=20 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install Poetry
ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

WORKDIR /opt
ENV PYTHONPATH="/opt:$PYTHONPATH"

################################
# BUILD
################################
FROM python-base as builder-base

RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    gnupg \
    ca-certificates \
    build-essential \
    git \
    nano \
    curl
    
RUN --mount=type=cache,target=/root/.cache \
    curl -sSL https://install.python-poetry.org | python - 
    
WORKDIR /opt
COPY poetry.lock pyproject.toml ./

RUN --mount=type=cache,target=/root/.cache \
    poetry install --no-root --only main

################################
# PRODUCTION
################################
FROM python-base as production

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates && \
    apt-get clean
    
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $VIRTUAL_ENV $VIRTUAL_ENV

WORKDIR /opt
COPY poetry.lock pyproject.toml ./
COPY app/ app/
COPY script/ script/
