"""Configuration settings for Densify AI"""
import os
from dotenv import load_dotenv

load_dotenv()

# Model Configuration
MODEL_PATH = os.getenv("MODEL_PATH", "model/yolov8n.pt")

# Crowd Density Thresholds
LOW_THRESHOLD = int(os.getenv("LOW_THRESHOLD", 10))
MEDIUM_THRESHOLD = int(os.getenv("MEDIUM_THRESHOLD", 30))

# Flask Configuration
DEBUG = os.getenv("DEBUG", "False") == "True"
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 5000))

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_DIR = os.getenv("LOG_DIR", "logs")
