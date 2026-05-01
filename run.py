#!/usr/bin/env python
"""Entry point for Densify AI Application"""
import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    from src.app import app
    app.run()
