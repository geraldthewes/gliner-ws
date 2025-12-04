#!/usr/bin/env python3
"""
Sample client program to test the evaluate endpoint of the NVIDIA Privacy Model Web Service.
This script demonstrates how to make requests to the /evaluate endpoint.
"""

import requests
import json
from typing import Dict, Any

# Base URL of the service - adjust if running on a different host/port
BASE_URL = "http://localhost:8000"

def test_evaluate_endpoint():
    """
    Test the evaluate endpoint with sample data
    """
    # Sample text to evaluate
    sample_text = "Contact me at john.doe@example.com or call 555-123-4567 for more information."
    
    # Request payload
    payload = {
        "text": sample_text,
        "labels": ["email", "phone_number"],
        "threshold": 0.5
    }
    
    try:
        # Send POST request to evaluate endpoint
        response = requests.post(
            f"{BASE_URL}/evaluate",
            json=payload,
            timeout=30
        )
        
        # Check if request was successful
        if response.status_code == 200:
            print("✅ Evaluation successful!")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Evaluation failed with status code {response.status_code}")
            print(f"Error: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def test_health_endpoint():
    """
    Test the health endpoint to verify service availability
    """
    try:
        response = requests.get(
            f"{BASE_URL}/health",
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ Health check successful!")
            print(f"Service status: {response.json()}")
        else:
            print(f"❌ Health check failed with status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def main():
    """
    Main function to run the client tests
    """
    print("🧪 Testing NVIDIA Privacy Model Web Service")
    print("=" * 50)
    
    # Test health endpoint first
    print("\n1. Testing health endpoint...")
    test_health_endpoint()
    
    # Test evaluate endpoint
    print("\n2. Testing evaluate endpoint...")
    test_evaluate_endpoint()
    
    print("\n" + "=" * 50)
    print("Test completed!")

if __name__ == "__main__":
    main()