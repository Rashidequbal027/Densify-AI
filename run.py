#!/usr/bin/env python
"""Entry point for Densify AI Application"""
import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    try:
        from src.app import app
        from src.config import HOST, PORT, DEBUG
        
        print("\n" + "="*60)
        print("🚀 Densify AI - Crowd Monitoring System")
        print("="*60)
        print(f"✓ Starting Flask server...")
        print(f"🌐 Open browser: http://{HOST}:{PORT}/")
        print("="*60 + "\n")
        
        app.run(host=HOST, port=PORT, debug=DEBUG, use_reloader=False)
    except ImportError as e:
        print(f"\n❌ Import Error: {e}")
        print("Make sure all dependencies are installed:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
