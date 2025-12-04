#!/usr/bin/env python3
"""
NVIDIA Privacy Model Web Service
A RESTful API for detecting PII and PHI using the NVIDIA GLiNER-PII model
"""

import os
import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import logging

# Add the models directory to the path so we can import model_manager
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import model manager and logging
from models.model_manager import ModelManager
from config.settings import get_config
from utils.logging import setup_logging

# Setup logging
logger = setup_logging()

# Initialize FastAPI app
app = FastAPI(
    title="NVIDIA Privacy Model Web Service",
    description="RESTful API for detecting PII and PHI using the NVIDIA GLiNER-PII model",
    version="0.1.0"
)

# Models for request/response
class Entity(BaseModel):
    text: str
    label: str
    start: int
    end: int
    score: float

class EvaluateRequest(BaseModel):
    text: str
    labels: Optional[List[str]] = None
    threshold: Optional[float] = 0.5

class EvaluateResponse(BaseModel):
    entities: List[Entity]

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    device: str

# Global variables for model management
model_manager = None
device = "cpu"

# Load configuration
config = get_config()

# Initialize model manager
try:
    model_manager = ModelManager(
        model_path=config["model_path"],
        model_download_url=config["model_download_url"],
        device=config["device"]
    )
    device = model_manager.device
    logger.info("Model manager initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize model manager: {e}")

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint to verify service availability and model readiness"""
    return HealthResponse(
        status="healthy",
        model_loaded=model_manager is not None,
        device=device
    )

@app.post("/evaluate", response_model=EvaluateResponse)
async def evaluate_pii_phi(request: EvaluateRequest):
    """Evaluate text for PII/PHI entities"""
    try:
        # Validate input
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")

        # Run prediction using the model manager
        if model_manager and model_manager.model:
            predictions = model_manager.predict(
                texts=[request.text],
                labels=request.labels,
                threshold=request.threshold
            )

            # Convert predictions to our response format
            entities = []
            for pred in predictions[0]:  # Since we only process one text
                entities.append(Entity(
                    text=pred["text"],
                    label=pred["label"],
                    start=pred["start"],
                    end=pred["end"],
                    score=pred["score"]
                ))

            return EvaluateResponse(entities=entities)
        else:
            raise HTTPException(status_code=500, detail="Model not loaded")

    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        raise HTTPException(status_code=500, detail=f"Evaluation failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)