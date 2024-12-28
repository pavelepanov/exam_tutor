FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


WORKDIR /exam_tutor

COPY requirements.txt pyproject.toml /exam_tutor/

COPY conf /exam_tutor/conf
COPY src /exam_tutor/src
COPY alembic.ini /exam_tutor

RUN --mount=type=cache,target=/root/.cache/pip \
    uv pip install -e . --system
