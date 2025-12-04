import os
import torch
from transformers import AutoTokenizer, AutoModel
from gliner import GLiNER
import logging

logger = logging.getLogger(__name__)

class ModelManager:
    def __init__(self, model_path: str, model_download_url: str, device: str = "auto"):
        self.model_path = model_path
        self.model_download_url = model_download_url
        self.device = device
        self.model = None
        self._ensure_model_exists()
        
    def _ensure_model_exists(self):
        """Ensure the model exists locally, downloading if necessary"""
        try:
            # Try to load the model
            self.model = GLiNER.from_pretrained(
                self.model_download_url,
                cache_dir=self.model_path
            )
            
            # Set device
            if self.device == "auto":
                self.device = "cuda" if torch.cuda.is_available() else "cpu"
            elif self.device == "cuda" and not torch.cuda.is_available():
                logger.warning("CUDA not available, falling back to CPU")
                self.device = "cpu"
                
            self.model.to(self.device)
            logger.info(f"Model loaded successfully on {self.device}")
            
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise
            
    def predict(self, texts: list, labels: list = None, threshold: float = 0.5):
        """Run prediction on texts"""
        if not self.model:
            raise RuntimeError("Model not loaded")
            
        try:
            # For batch processing, we'll need to handle it properly
            results = []
            
            # Simple implementation for now - in a real scenario, 
            # this would handle batching and more complex logic
            for text in texts:
                predictions = self.model.predict(text, labels=labels, threshold=threshold)
                results.append(predictions)
                
            return results
        except Exception as e:
            logger.error(f"Prediction failed: {e}")
            raise