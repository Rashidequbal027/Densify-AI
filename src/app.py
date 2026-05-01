"""Main Flask application for Densify AI"""
import logging
import cv2
import os
from pathlib import Path
from flask import Flask, render_template, Response
from src.utils.detector import detect_people
from src.utils.density import get_density
from src.config import DEBUG, HOST, PORT, LOG_LEVEL, LOG_DIR

# Setup logging
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'{LOG_DIR}/densify_ai.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Get base directory
BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(__name__, 
            template_folder=str(BASE_DIR / 'templates'),
            static_folder=str(BASE_DIR / 'static'))
app.config['DEBUG'] = DEBUG

cap = None


def initialize_camera():
    """Initialize camera capture"""
    global cap
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            logger.error("Failed to open camera")
            return False
        logger.info("Camera initialized successfully")
        return True
    except Exception as e:
        logger.error(f"Error initializing camera: {str(e)}")
        return False


def generate_frames():
    """Generate video frames with detection"""
    try:
        while True:
            if cap is None or not cap.isOpened():
                logger.warning("Camera not available")
                break

            success, frame = cap.read()
            if not success:
                logger.warning("Failed to read frame")
                break

            # Resize for faster processing
            frame = cv2.resize(frame, (640, 480))

            count, boxes = detect_people(frame)
            density = get_density(count)

            # Draw bounding boxes
            for (x1, y1, x2, y2) in boxes:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Put text
            cv2.putText(frame, f'Count: {count}', (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(frame, f'Status: {density}', (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Encode frame
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                logger.error("Failed to encode frame")
                continue

            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    except Exception as e:
        logger.error(f"Error in generate_frames: {str(e)}")
    finally:
        if cap is not None:
            cap.release()
            logger.info("Camera released")


@app.route('/')
def index():
    """Home page"""
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering index: {str(e)}")
        return "Error loading page", 500


@app.route('/video')
def video():
    """Video stream endpoint"""
    try:
        return Response(generate_frames(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        logger.error(f"Error in video route: {str(e)}")
        return "Error streaming video", 500


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    logger.warning(f"404 error: {e}")
    return {"error": "Not found"}, 404


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    logger.error(f"500 error: {e}")
    return {"error": "Internal server error"}, 500


if __name__ == "__main__":
    logger.info("Starting Densify AI Application")
    if initialize_camera():
        app.run(host=HOST, port=PORT, debug=DEBUG)
    else:
        logger.error("Failed to start application: Camera initialization failed")
