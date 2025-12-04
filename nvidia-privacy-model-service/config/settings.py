import os

# Default configuration values
CONFIG = {
    "model_path": os.path.join(os.path.expanduser("~"), ".cache", "gliner"),
    "model_download_url": "nvidia/GliNER-PII",
    "threshold_default": 0.5,
    "max_batch_size": 100,
    "device": "auto"  # auto, cuda, cpu
}

# Environment variable overrides
def get_config():
    """Get configuration with environment variable overrides"""
    config = CONFIG.copy()
    
    # Override with environment variables if they exist
    if "MODEL_PATH" in os.environ:
        config["model_path"] = os.environ["MODEL_PATH"]
        
    if "MODEL_DOWNLOAD_URL" in os.environ:
        config["model_download_url"] = os.environ["MODEL_DOWNLOAD_URL"]
        
    if "THRESHOLD_DEFAULT" in os.environ:
        try:
            config["threshold_default"] = float(os.environ["THRESHOLD_DEFAULT"])
        except ValueError:
            pass  # Keep default if invalid
            
    if "MAX_BATCH_SIZE" in os.environ:
        try:
            config["max_batch_size"] = int(os.environ["MAX_BATCH_SIZE"])
        except ValueError:
            pass  # Keep default if invalid
            
    if "DEVICE" in os.environ:
        config["device"] = os.environ["DEVICE"]
        
    return config