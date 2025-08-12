# Dockerfile

# Use official Python image
FROM python:3.10-slim

# Environment setup
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run with Gunicorn (for production)
CMD ["gunicorn", "ims.wsgi:application", "--bind", "0.0.0.0:8000"]
