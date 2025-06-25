# Use official Python 3.9 base image
FROM python:3.9-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install poetry and the package
RUN curl -sSL https://install.python-poetry.org | python3 -

# Default command
CMD ["bash"]
