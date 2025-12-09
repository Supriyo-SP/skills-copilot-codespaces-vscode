"""Configuration and constants for the CLI application."""
import os
from pathlib import Path

# Application paths
APP_DIR = Path.home() / '.skills-copilot'
CONFIG_FILE = APP_DIR / 'config.json'
DATA_DIR = APP_DIR / 'data'

# Create directories if they don't exist
APP_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

# Application metadata
APP_NAME = "Skills Copilot"
APP_VERSION = "1.0.0"
