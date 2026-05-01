"""Tests for Densify AI detector module"""
import pytest
from src.utils.detector import PeopleDetector
import numpy as np


def test_detector_initialization():
    """Test detector initialization"""
    detector = PeopleDetector()
    assert detector is not None
    assert detector.model is not None


def test_detect_people():
    """Test people detection with dummy frame"""
    detector = PeopleDetector()
    # Create a dummy frame
    dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    
    count, boxes = detector.detect_people(dummy_frame)
    assert isinstance(count, int)
    assert isinstance(boxes, list)
    assert count >= 0
