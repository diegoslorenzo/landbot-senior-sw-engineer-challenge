# Use the official Python image based on Debian Slim
FROM python:3.11.4-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Install required system dependencies for Django and PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the working directory
COPY requirements.txt .

# Upgrade pip and install Python dependencies from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire application to the container
COPY . .

# Create a non-root user to run the application
RUN addgroup --system appgroup && adduser --system --group appuser

# Switch to the non-root user
USER appuser

# Expose the port the Django app will run on
EXPOSE 8000

# Default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
