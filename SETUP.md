# 📋 Complete Setup Guide - Densify AI

## System Requirements

- Python 3.8+
- Webcam or video input source
- 4GB RAM minimum
- Modern web browser (Chrome, Firefox, Safari, Edge)

---

## Installation Methods

### Method 1: Local Installation (Recommended for Development)

#### 1. Clone Repository
```bash
cd ~/Desktop
git clone https://github.com/Rashidequbal027/Densify-AI.git
cd Densify-AI
```

#### 2. Create Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Run Application
```bash
# macOS / Linux
./run.sh

# Windows
run.bat

# Or directly
python run.py
```

#### 5. Access Application
Open browser and go to: `http://127.0.0.1:5000/`

---

### Method 2: Docker (Production Ready)

#### Prerequisites
- Docker installed
- Docker Compose installed

#### Steps
```bash
cd Densify-AI

# Build and run
docker-compose up --build

# Access application
# Open browser: http://localhost:5000/
```

---

### Method 3: Development Mode

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Run with auto-reload
python run.py
```

---

## Configuration

### Environment Variables

Create `.env` file in project root:

```env
# Flask Configuration
DEBUG=True
HOST=127.0.0.1
PORT=5000

# Model Configuration
MODEL_PATH=model/yolov8n.pt

# Crowd Thresholds
LOW_THRESHOLD=10
MEDIUM_THRESHOLD=30

# Logging
LOG_LEVEL=INFO
LOG_DIR=logs
```

### Using .env Template

```bash
cp .env.example .env
# Edit .env with your settings
```

---

## Verification

### Check Installation
```bash
python -c "import cv2, flask, ultralytics; print('✓ All dependencies installed')"
```

### Run Tests
```bash
pytest tests/ -v
```

### Check Logs
```bash
tail -f logs/densify_ai.log
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'dotenv'"
**Solution:**
```bash
pip install python-dotenv
```

### Issue: Camera Not Detected
**Solution:**
- Check if camera is connected and accessible
- Try another application to verify camera works
- On Linux, might need: `sudo apt-get install libsm6 libxext6`

### Issue: "Port 5000 already in use"
**Solution:**
Edit `.env` file:
```env
PORT=5001  # or any available port
```

### Issue: Import errors in IDE
**Solution:**
- Activate virtual environment: `source venv/bin/activate`
- Set Python interpreter in IDE to use venv Python

### Issue: Templates/Static files not loading
**Solution:**
- Make sure you're running from project root directory
- Check file paths in `src/app.py` are correct

---

## File Structure

```
Densify-AI/
├── src/                    # Source code
│   ├── app.py             # Main Flask app
│   ├── config.py          # Configuration
│   └── utils/             # Helper modules
├── templates/              # HTML templates
├── static/                 # CSS, JS files
├── tests/                  # Test suite
├── logs/                   # Application logs
├── data/                   # Data folder
├── .env                    # Environment config
├── requirements.txt        # Dependencies
├── run.py                  # Entry point
├── Dockerfile              # Docker config
└── docker-compose.yml      # Compose config
```

---

## Next Steps

1. ✅ Install and run application
2. 📊 Open http://127.0.0.1:5000/
3. 🎥 Allow camera access
4. 🧪 Run tests with pytest
5. 🐳 Try Docker deployment

---

## Additional Resources

- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Docker Documentation](https://docs.docker.com/)

---

**Happy coding! 🚀**
