# 🚀 Quick Start Guide - Densify AI

## Get Started in 2 Minutes

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Application
```bash
python run.py
```

### 3️⃣ Open in Browser
```
http://127.0.0.1:5000/
```

---

## 🖥️ Platform-Specific Instructions

### macOS / Linux
```bash
chmod +x run.sh
./run.sh
```

### Windows
```bash
run.bat
```

---

## 🐳 Using Docker

```bash
docker-compose up --build
```

Then open: `http://localhost:5000/`

---

## 🧪 Run Tests

```bash
pip install -r requirements-dev.txt
pytest tests/ -v
```

---

## ⚙️ Configure Environment

Edit `.env` file:
```env
DEBUG=True          # Enable debug mode
HOST=127.0.0.1      # Server host
PORT=5000           # Server port
LOG_LEVEL=INFO      # Logging level
```

---

## 🔧 Troubleshooting

### Import Error: No module named 'dotenv'
```bash
pip install python-dotenv
```

### Camera Not Found
- Check if camera is accessible
- Use `--no-camera` flag for testing

### Port Already in Use
Change PORT in `.env`:
```env
PORT=5001
```

---

## 📱 Features

✅ Real-time person detection  
✅ Crowd density classification  
✅ Live video streaming  
✅ Production-grade code structure  
✅ Error handling & logging  
✅ Docker support  

---

**Need help?** Check `README.md` for full documentation.
