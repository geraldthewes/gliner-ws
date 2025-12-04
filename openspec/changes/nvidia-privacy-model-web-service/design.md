# Design: NVIDIA Privacy Model Web Service

## Architecture Overview

The NVIDIA Privacy Model Web Service is designed as a modular, scalable REST API that leverages the NVIDIA GLiNER-PII model for privacy information detection. The service follows a layered architecture with clear separation of concerns and is containerized for easy deployment.

## Components

### 1. Service Layer
- FastAPI application with routing
- Request/response handling
- Input validation and sanitization
- Error response formatting

### 2. Model Layer
- GLiNER model manager
- Automatic model downloading and caching
- Model initialization and warm-up
- Batch processing capabilities

### 3. Utility Layer
- Configuration management
- Logging and monitoring
- Health check utilities
- Metrics collection

## API Endpoints

### Health Check Endpoint
- **Path**: `/health`
- **Method**: GET
- **Purpose**: Verify service availability and model readiness
- **Response**: JSON with service status and model information

### Evaluation Endpoint
- **Path**: `/evaluate`
- **Method**: POST
- **Purpose**: Analyze text for PII/PHI information
- **Request Body**: 
  ```json
  {
    "text": "input text to analyze",
    "labels": ["email", "phone_number"],
    "threshold": 0.5
  }
  ```
- **Response**: 
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

## Containerization Design

### Base Image
- **Python 3.12** as the base image
- Optimized for **NVIDIA GPU** environments
- Support for **CPU fallback** when GPU is not available

### Container Features
- **Multi-stage build** for optimal size
- **GPU acceleration** when available
- **CPU fallback** for environments without NVIDIA GPUs
- **Optimized runtime** for privacy scanning workloads

## Model Management

### Auto-download
- On first startup, service downloads NVIDIA GLiNER-PII model
- Model is cached locally for subsequent startups
- Version checking for updates

### Hardware Detection
- Service detects available hardware (GPU vs CPU)
- Automatically selects optimal execution backend
- Falls back to CPU when GPU is unavailable

## Configuration Options

### Environment Variables
- `MODEL_PATH`: Custom model storage location
- `MODEL_DOWNLOAD_URL`: Alternative model download source
- `THRESHOLD_DEFAULT`: Default confidence threshold
- `MAX_BATCH_SIZE`: Maximum number of texts to process in batch
- `DEVICE`: Force device selection (cuda/cpu)

### Runtime Parameters
- `threshold`: Minimum confidence score for entity detection
- `labels`: Specific PII/PHI labels to detect
- `batch_size`: Number of texts to process together

## Error Handling

### Common Errors
- Invalid input text
- Model loading failures
- Out-of-memory conditions
- Invalid configuration values

### Response Format
All errors return standardized JSON responses:
```json
{
  "error": "description of error",
  "code": "error code"
}
```

## Performance Considerations

### Caching Strategy
- Model is loaded once at startup
- Results from previous evaluations may be cached for performance but in a later version
- Memory usage optimized for batch processing

### Hardware Optimization
- GPU acceleration when available
- CPU fallback for environments without NVIDIA GPUs
- Efficient memory management for both backends

### Scalability
- Stateless design allows horizontal scaling
- Containerized for easy deployment
- Support for load balancing

## Security Considerations

### Input Sanitization
- All input text is validated for length and format
- Potential injection points are handled appropriately
- Sensitive data is not logged in plain text

### Access Control
- Basic authentication can be added
- Rate limiting for API endpoints
- HTTPS support (recommended)

## Monitoring and Logging

### Service Logs
- Request/response logging
- Performance metrics
- Error tracking
- Model loading events

### Health Metrics
- Service uptime
- Model readiness status
- Processing throughput
- Memory usage
- Hardware utilization (GPU/CPU)

## Deployment Options

### Containerization
- **Docker** container with lightweight base image
- **NVIDIA Container Toolkit** support for GPU acceleration
- **CPU fallback** when GPU is not available
- **Multi-platform** compatibility (Linux, Windows, macOS)

### Runtime Environments
- **NVIDIA GPU servers** with CUDA support
- **CPU-only servers** with fallback capability
- **Cloud environments** with GPU instances
