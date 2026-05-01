@echo off
REM Run script for Densify AI (Windows)

echo 🚀 Starting Densify AI...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✓ %PYTHON_VERSION%

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements
echo 📥 Installing dependencies...
pip install -q -r requirements.txt

REM Run the application
echo ✨ Starting Flask application...
echo 🌐 Open browser: http://127.0.0.1:5000/
echo.

python run.py
