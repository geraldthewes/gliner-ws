FROM nvidia/cuda:11.8-runtime-ubuntu22.04

# Set working directory
WORKDIR /app

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create logs directory
RUN mkdir -p logs

# Define environment variables
ENV MODEL_PATH=~/.cache/gliner
ENV MODEL_DOWNLOAD_URL=nvidia/GliNER-PII
ENV THRESHOLD_DEFAULT=0.5
ENV MAX_BATCH_SIZE=100
ENV DEVICE=auto
ENV LOG_LEVEL=INFO
ENV PORT=8000

# Expose port
EXPOSE 8000

# Run the application
CMD ["python3", "main.py"]