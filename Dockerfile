FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libpulse0 \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY ProgramToHologram/ ./ProgramToHologram/
COPY .env .

# Set environment variables from .env file
ENV PYTHONPATH=/app

# Expose port if needed
EXPOSE 8000

# Run the application
CMD ["python", "ProgramToHologram/main.py"]