"""Shared pytest setup for the project tests."""

import sys
from pathlib import Path


# Make the project root importable so tests can import the src package.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
