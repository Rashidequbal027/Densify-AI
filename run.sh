#!/bin/bash
# Run script for Densify AI

set -e

echo "🚀 Starting Densify AI..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

echo "✓ Python version: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Run the application
echo "✨ Starting Flask application..."
echo "🌐 Open browser: http://127.0.0.1:5000/"
echo ""

python run.py
