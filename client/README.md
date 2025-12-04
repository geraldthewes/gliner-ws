# Client Sample for NVIDIA Privacy Model Web Service

This directory contains a sample client program that demonstrates how to interact with the NVIDIA Privacy Model Web Service API.

## Features

- Tests the `/evaluate` endpoint
- Tests the `/health` endpoint
- Demonstrates proper request formatting
- Includes error handling

## Usage

1. First, ensure the NVIDIA Privacy Model Web Service is running:
   ```bash
   cd /home/gerald/repos/gliner-ws/nvidia-privacy-model-service
   python main.py
   ```

2. Then run the client:
   ```bash
   cd /home/gerald/repos/gliner-ws/client
   python sample_client.py
   ```

## Dependencies

The client requires the following dependencies:
- `requests` (>=2.25.0)

Install them with:
```bash
pip install -r requirements.txt
```

## Example Output

When running successfully, you'll see output similar to:
```
🧪 Testing NVIDIA Privacy Model Web Service
==================================================

1. Testing health endpoint...
✅ Health check successful!
Service status: {'status': 'healthy', 'model_loaded': True, 'device': 'cuda'}

2. Testing evaluate endpoint...
✅ Evaluation successful!
Response: {'entities': [{'text': 'john.doe@example.com', 'label': 'email', 'start': 15, 'end': 31, 'score': 0.95}, {'text': '555-123-4567', 'label': 'phone_number', 'start': 52, 'end': 63, 'score': 0.92}]}
==================================================
Test completed!
```