# Specification: NVIDIA Privacy Model Web Service

## Overview
This specification defines the requirements for implementing a self-contained web service that utilizes the NVIDIA GLiNER-PII model for detecting and classifying Personally Identifiable Information (PII) and Protected Health Information (PHI). The service is containerized for deployment on servers with NVIDIA GPUs but includes CPU fallback capability.

## ADDED Requirements

### 1. Service Core Functionality
#### Scenario: Service Initialization
- The service must automatically download the NVIDIA GLiNER-PII model if not present
- The service must cache the model locally for subsequent startups
- The service must initialize the model on startup for optimal performance
- The service must detect available hardware (GPU vs CPU) at startup

#### Scenario: Health Endpoint
- The service must expose a `/health` endpoint
- The `/health` endpoint must return a JSON response with service status
- The `/health` endpoint must indicate model readiness
- The `/health` endpoint must include version information and hardware status

#### Scenario: Evaluation Endpoint
- The service must expose an `/evaluate` endpoint
- The `/evaluate` endpoint must accept POST requests with JSON payload
- The `/evaluate` endpoint must process text for PII/PHI detection
- The `/evaluate` endpoint must return structured results with entities, labels, positions, and scores

### 2. API Interface Requirements
#### Scenario: Input Validation
- The `/evaluate` endpoint must validate input text
- The `/evaluate` endpoint must validate labels parameter if provided
- The `/evaluate` endpoint must validate threshold parameter if provided
- The `/evaluate` endpoint must reject invalid payloads

#### Scenario: Response Format
- The `/evaluate` endpoint must return JSON with consistent structure
- The response must include an array of detected entities
- Each entity must include text, label, start position, end position, and score
- The response must include metadata about the processing

### 3. Model Management Requirements
#### Scenario: Model Download
- The service must download the NVIDIA GLiNER-PII model from Hugging Face
- The service must handle download failures gracefully
- The service must store the model in a persistent location
- The service must verify model integrity after download

#### Scenario: Model Caching
- The service must cache downloaded models for reuse
- The service must support model versioning
- The service must handle model updates when available

### 4. Containerization Requirements
#### Scenario: Lightweight Container
- The service must be containerized with a lightweight Python 3.12 base image
- The container must be optimized for minimal size and performance
- The container must support NVIDIA GPU acceleration
- The container must include CPU fallback capability

#### Scenario: Hardware Detection
- The service must detect available hardware (NVIDIA GPU vs CPU) at startup
- The service must automatically select the optimal execution backend
- The service must fall back to CPU when GPU is not available
- The service must report hardware status in health checks

### 5. Performance Requirements
#### Scenario: Batch Processing
- The service must support batch processing of multiple texts
- The service must maintain performance for batch operations
- The service must optimize processing based on available hardware

#### Scenario: Resource Management
- The service must manage memory usage efficiently
- The service must handle out-of-memory conditions gracefully
- The service must optimize model inference performance for both GPU and CPU

### 6. Security Requirements
#### Scenario: Input Sanitization
- The service must sanitize input text for security
- The service must prevent injection attacks
- The service must handle large inputs appropriately

#### Scenario: Data Protection
- The service must not log sensitive information in plain text
- The service must protect model files from unauthorized access
- The service must implement secure communication protocols

## MODIFIED Requirements

### 1. Existing API Behavior
#### Scenario: Enhanced Error Handling
- All API endpoints must return standardized error responses
- Error responses must include descriptive messages and error codes
- Error responses must be consistent across all endpoints

### 2. Hardware Support
#### Scenario: GPU Acceleration with Fallback
- The service must support NVIDIA GPU acceleration when available
- The service must fall back to CPU processing when GPU is not available
- The service must detect and report hardware capabilities in health checks

## REMOVED Requirements

### 1. Legacy Features
- Removed support for older model versions
- Removed deprecated API endpoints
- Removed unused configuration options

## Implementation Notes

### Technology Stack
- Framework: FastAPI
- Model Library: GLiNER
- Runtime: Python 3.12
- Containerization: Docker with lightweight base image
- GPU Support: NVIDIA Container Toolkit

### Deployment Options
- Standalone Python service
- Containerized deployment (Docker)
- Cloud-native deployment (Kubernetes)
- GPU-accelerated servers with NVIDIA GPUs
- CPU-only servers with fallback capability

### Monitoring and Logging
- Service health monitoring
- Performance metrics collection
- Audit logging for security purposes
- Hardware utilization tracking (GPU/CPU)