"""Crowd density classification module"""
import logging
from src.config import LOW_THRESHOLD, MEDIUM_THRESHOLD

logger = logging.getLogger(__name__)


class DensityClassifier:
    """Classifies crowd density based on person count"""

    def __init__(self, low_threshold=LOW_THRESHOLD, medium_threshold=MEDIUM_THRESHOLD):
        """Initialize with thresholds"""
        self.low_threshold = low_threshold
        self.medium_threshold = medium_threshold

    def get_density(self, count):
        """
        Classify crowd density
        
        Args:
            count: Number of people detected
            
        Returns:
            dict: Density status and color code
        """
        if count < self.low_threshold:
            return {
                "status": "Low Crowd",
                "level": "low",
                "color": (0, 255, 0)  # Green
            }
        elif count < self.medium_threshold:
            return {
                "status": "Medium Crowd",
                "level": "medium",
                "color": (0, 165, 255)  # Orange
            }
        else:
            return {
                "status": "High Crowd",
                "level": "high",
                "color": (0, 0, 255)  # Red
            }


# Initialize classifier
classifier = DensityClassifier()


def get_density(count):
    """Wrapper function for backward compatibility"""
    return classifier.get_density(count)["status"]
