"""Tests for Densify AI density classifier"""
import pytest
from src.utils.density import DensityClassifier


def test_density_low():
    """Test low density classification"""
    classifier = DensityClassifier()
    result = classifier.get_density(5)
    assert result["level"] == "low"
    assert result["status"] == "Low Crowd"


def test_density_medium():
    """Test medium density classification"""
    classifier = DensityClassifier()
    result = classifier.get_density(15)
    assert result["level"] == "medium"
    assert result["status"] == "Medium Crowd"


def test_density_high():
    """Test high density classification"""
    classifier = DensityClassifier()
    result = classifier.get_density(50)
    assert result["level"] == "high"
    assert result["status"] == "High Crowd"
