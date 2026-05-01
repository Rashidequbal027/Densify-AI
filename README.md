# Densify AI - Smart Crowd Monitoring & Estimation Platform

## 📌 Overview
Densify AI is a production-grade real-time crowd monitoring system that uses YOLOv8 and OpenCV to detect and count people in video streams with proper error handling, logging, and configuration management.

## 🚀 Features
- ✅ Real-time people detection with YOLOv8
- ✅ Crowd counting and density classification
- ✅ Web dashboard using Flask
- ✅ Comprehensive logging and error handling
- ✅ Docker support for easy deployment
- ✅ Unit tests with pytest
- ✅ Environment-based configuration
- ✅ CI/CD ready with GitHub Actions

## 🛠 Tech Stack
- Python 3.10+
- OpenCV (4.8.1.78)
- YOLOv8 (8.0.198)
- Flask (3.0.0)
- Docker & Docker Compose
- pytest for testing

## 📁 Project Structure
```
src/                    # Source code
├── app.py             # Main Flask application
├── config.py          # Configuration management
└── utils/             # Utility modules
    ├── detector.py    # YOLO detection
    └── density.py     # Density classification
tests/                 # Test suite
data/                  # Data folder for uploads
logs/                  # Application logs
```

## ⚙️ Installation & Setup

### Option 1: Local Installation
```bash
# Clone the repository
git clone https://github.com/Rashidequbal027/Densify-AI.git
cd Densify-AI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Run application
python run.py
```

### Option 2: Docker
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build manually
docker build -t densify-ai .
docker run -p 5000:5000 densify-ai
```

## 🚀 How to Run

1. **Setup environment:**
   ```bash
   cp .env.example .env
   ```

2. **Run the application:**
   ```bash
   python run.py
   ```

3. **Open in browser:**
   ```
   http://127.0.0.1:5000/
   ```

## 🧪 Testing

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src/
```

## ⚡ Configuration

Edit `.env` file for configuration:
```env
# Model
MODEL_PATH=model/yolov8n.pt

# Thresholds
LOW_THRESHOLD=10
MEDIUM_THRESHOLD=30

# Flask
DEBUG=True
HOST=127.0.0.1
PORT=5000

# Logging
LOG_LEVEL=INFO
LOG_DIR=logs
```

## 📊 Density Levels
- **Low Crowd:** < 10 people (Green)
- **Medium Crowd:** 10-30 people (Orange)
- **High Crowd:** > 30 people (Red)

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web dashboard |
| `/video` | GET | Video stream endpoint |

## 🔍 Logs

Application logs are saved in `logs/densify_ai.log`

## 🤝 Contributing

Contributions are welcome! Please follow:
1. Create a new branch
2. Make changes
3. Add tests
4. Submit pull request

## 📄 License
MIT License

## 👨‍💻 Author
**Rashid Equbal**
