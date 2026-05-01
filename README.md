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
Densify-AI/
├── src/                          # Source code (main application)
│   ├── __init__.py              # Package initialization
│   ├── app.py                   # Main Flask application with logging
│   ├── config.py                # Configuration management (env vars)
│   └── utils/                   # Utility modules
│       ├── __init__.py
│       ├── detector.py          # YOLO detection logic (PeopleDetector class)
│       └── density.py           # Density classification (DensityClassifier class)
│
├── templates/                    # HTML templates
│   └── index.html               # Modern dashboard UI
│
├── static/                       # Static files (CSS, JavaScript)
│   └── style.css                # Responsive styling
│
├── tests/                        # Test suite (pytest)
│   ├── __init__.py
│   ├── conftest.py              # pytest configuration
│   ├── test_detector.py         # Detector module tests
│   └── test_density.py          # Density classifier tests
│
├── data/                         # Data folder for uploads/datasets
│   └── .gitkeep                 # Git tracking placeholder
│
├── logs/                         # Application logs directory
│   └── .gitkeep                 # Git tracking placeholder
│
├── model/                        # Machine learning models
│   └── yolov8n.pt               # YOLOv8 nano model (pretrained COCO)
│
├── .github/workflows/            # CI/CD pipelines
│   └── tests.yml                # GitHub Actions workflow
│
├── .env                          # Environment variables (local, ignored by git)
├── .env.example                  # Environment template (version control)
├── .gitignore                    # Git ignore patterns
│
├── Dockerfile                    # Docker configuration
├── docker-compose.yml            # Docker Compose orchestration
│
├── requirements.txt              # Python dependencies (production)
├── requirements-dev.txt          # Dev dependencies (pytest, etc)
│
├── run.py                        # Python entry point (main script)
├── run.sh                        # Bash startup script (macOS/Linux)
├── run.bat                       # Batch startup script (Windows)
│
├── README.md                     # Main documentation
├── QUICKSTART.md                 # 2-minute quick start guide
├── SETUP.md                      # Detailed setup & installation
├── CONTRIBUTING.md               # Contribution guidelines
├── PROJECT_STRUCTURE.md          # Detailed structure documentation
├── LICENSE                       # MIT License
└── .git/                         # Git repository
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

### Quick Start (Recommended)
Choose based on your operating system:

**macOS / Linux:**
```bash
./run.sh
```

**Windows:**
```bash
run.bat
```

**Any OS (Python):**
```bash
python run.py
```

### Manual Steps
1. **Setup environment:**
   ```bash
   cp .env.example .env
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python run.py
   ```

4. **Open in browser:**
   ```
   http://127.0.0.1:5000/
   ```

### Docker
```bash
# Build and run with Docker Compose
docker-compose up --build

# Access the application
# Open browser: http://localhost:5000/
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

## 📚 Documentation

| File | Purpose |
|------|---------|
| **README.md** | Main documentation (you are here) |
| **QUICKSTART.md** | 2-minute quick start guide |
| **SETUP.md** | Detailed installation & configuration |
| **CONTRIBUTING.md** | Guidelines for contributors |
| **PROJECT_STRUCTURE.md** | Detailed structure explanation |

## 🤝 Contributing

Contributions are welcome! Please follow the [CONTRIBUTING.md](CONTRIBUTING.md) guide:
1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make changes and add tests
4. Commit with meaningful messages
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

## 📄 License
MIT License

## 👨‍💻 Author
**Rashid Equbal**
