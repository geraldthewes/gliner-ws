#!/usr/bin/env python3
"""
Simple script to run the NVIDIA Privacy Model Web Service
"""

import subprocess
import sys
import os

def main():
    print("Starting NVIDIA Privacy Model Web Service...")
    
    # Change to the service directory
    service_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Run the service with uvicorn
        cmd = [
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--reload"
        ]
        
        print(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd, cwd=service_dir, check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error running service: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nService stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()