"""Utility functions for the CLI application."""
import json
from pathlib import Path
from config import CONFIG_FILE, DATA_DIR


def load_config():
    """Load configuration from file."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_config(config):
    """Save configuration to file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)


def load_json_file(file_path):
    """Load JSON from a file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in file: {file_path}")


def save_json_file(file_path, data):
    """Save data as JSON to a file."""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def read_file(file_path):
    """Read content from a file."""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")


def write_file(file_path, content):
    """Write content to a file."""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(content)
