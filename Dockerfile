# Use official Python 3.10 slim image
FROM python:3.10-slim

# Environment variables for Poetry
ENV POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH" \
    POETRY_VIRTUALENVS_CREATE=false

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set working directory (will be overridden by volume mount)
WORKDIR /workspace

# Default command (VSCode will override this if needed)
CMD [ "bash" ]
