import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Signature database path
SIGNATURES_PATH = BASE_DIR / "signatures" / "hash_signatures.json"

# Analysis defaults
DEFAULT_CONFIDENCE_THRESHOLD = 0.1

# Reporting defaults
OUTPUT_FORMATS = ["text", "json", "markdown"]
