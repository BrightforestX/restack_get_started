FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y nginx

RUN pip install poetry

COPY pyproject.toml ./

COPY . .

# Configure poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Expose port 80
EXPOSE 80

# Start Poetry
CMD poetry run services