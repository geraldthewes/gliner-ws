# NVIDIA Privacy Model Web Service

A RESTful web service that utilizes the NVIDIA GLiNER-PII model for detecting and classifying Personally Identifiable Information (PII) and Protected Health Information (PHI) in text.

## Features

- REST API endpoints for privacy scanning
- Health check endpoint
- Automatic model downloading and caching
- Support for batch processing
- Configurable thresholds and label filtering
- Comprehensive logging and monitoring
- Containerized deployment for Linux

## API Endpoints

### Health Check
```
GET /health
```
Returns service status and model information.

### Evaluation
```
POST /evaluate
```

Request body:
```json
{
  "text": "input text to analyze",
  "labels": ["email", "phone_number"],
  "threshold": 0.5
}
```

Response:
```json
{
  "entities": [
    {
      "text": "detected entity",
      "label": "entity type",
      "start": 0,
      "end": 10,
      "score": 0.95
    }
  ]
}
```

## Installation

### Prerequisites
- Python 3.12+
- NVIDIA GPU with CUDA support (optional, CPU fallback available)

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd nvidia-privacy-model-service

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Environment variables:
- `MODEL_PATH`: Custom model storage location
- `MODEL_DOWNLOAD_URL`: Alternative model download source  
- `THRESHOLD_DEFAULT`: Default confidence threshold
- `MAX_BATCH_SIZE`: Maximum number of texts to process in batch
- `DEVICE`: Force device selection (cuda/cpu)

## Running the Service

```bash
# Run with uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

# Or run directly
python main.py
```

## Containerization

Build and run with Docker:
```bash
# Build the image
docker build -t nvidia-privacy-model-service .

# Run the container
docker run --gpus all nvidia-privacy-model-service
```

## Development

### Project Structure
```
nvidia-privacy-model-service/
├── main.py              # Main application entrypoint
├── requirements.txt     # Dependencies
├── Dockerfile         # Container configuration
├── config/
│   └── settings.py    # Configuration management
├── models/
│   └── model_manager.py # Model loading and processing
└── utils/
    └── logging.py     # Logging configuration
```

## License

This project is licensed under the NVIDIA license.