#!/bin/bash

# Setup script for NVIDIA Privacy Model Web Service

echo "Setting up NVIDIA Privacy Model Web Service..."

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete!"
echo "To run the service:"
echo "  source venv/bin/activate"
echo "  python main.py"