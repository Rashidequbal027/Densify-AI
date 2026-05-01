"""People detection module using YOLOv8"""
import logging
from ultralytics import YOLO
from src.config import MODEL_PATH

logger = logging.getLogger(__name__)


class PeopleDetector:
    """Detects people in video frames using YOLOv8"""

    def __init__(self, model_path=MODEL_PATH):
        """Initialize the detector with YOLO model"""
        try:
            self.model = YOLO(model_path)
            logger.info(f"Model loaded successfully from {model_path}")
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise

    def detect_people(self, frame):
        """
        Detect people in a frame
        
        Args:
            frame: Input video frame
            
        Returns:
            tuple: (count of people, list of bounding boxes)
        """
        try:
            results = self.model(frame)
            count = 0
            boxes_list = []

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    cls = int(box.cls[0])
                    if cls == 0:  # person class
                        count += 1
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        boxes_list.append((x1, y1, x2, y2))

            return count, boxes_list
        except Exception as e:
            logger.error(f"Error during detection: {str(e)}")
            return 0, []


# Initialize detector
detector = PeopleDetector()


def detect_people(frame):
    """Wrapper function for backward compatibility"""
    return detector.detect_people(frame)
