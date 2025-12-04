#!/bin/bash

# Script to run tests for the NVIDIA Privacy Model Web Service

echo "Running tests for NVIDIA Privacy Model Web Service..."

# Change to the service directory
cd "$(dirname "$0")"

# Run Python tests
python -m pytest tests/ -v

echo "Tests completed."