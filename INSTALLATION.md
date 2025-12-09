# Installation and Usage Guide for Local System

## Option 1: Clone and Run Directly

### Step 1: Clone the Repository
```bash
git clone https://github.com/Supriyo-SP/skills-copilot-codespaces-vscode.git
cd skills-copilot-codespaces-vscode
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the CLI
```bash
python -m src.main --help
python -m src.main math add 10 20
python -m src.main text uppercase hello
```

---

## Option 2: Install as a Command-Line Tool (Recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Supriyo-SP/skills-copilot-codespaces-vscode.git
cd skills-copilot-codespaces-vscode
```

### Step 2: Install in Development Mode
```bash
pip install -e .
```

This installs the package and creates the `skills-copilot` command globally.

### Step 3: Use the Command Anywhere
```bash
# Now you can use it from any directory
skills-copilot --help
skills-copilot math add 15 25
skills-copilot text uppercase "hello world"
skills-copilot file read /path/to/file.txt
```

---

## Option 3: Install from PyPI (When Published)

Once the package is published to PyPI:
```bash
pip install skills-copilot
skills-copilot --help
```

---

## Full Installation Steps for Your Local Machine

### Windows PowerShell / Command Prompt

```powershell
# 1. Clone the repository
git clone https://github.com/Supriyo-SP/skills-copilot-codespaces-vscode.git
cd skills-copilot-codespaces-vscode

# 2. Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install as editable package
pip install -e .

# 5. Run the CLI
skills-copilot --help
```

### macOS / Linux

```bash
# 1. Clone the repository
git clone https://github.com/Supriyo-SP/skills-copilot-codespaces-vscode.git
cd skills-copilot-codespaces-vscode

# 2. Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install as editable package
pip install -e .

# 5. Run the CLI
skills-copilot --help
```

---

## Quick Examples After Installation

```bash
# Math operations
skills-copilot math add 100 200 300
skills-copilot math multiply 12 5
skills-copilot math sqrt 144
skills-copilot math factorial 5

# Text operations
skills-copilot text uppercase "hello world"
skills-copilot text reverse "python"
skills-copilot text word-count "the quick brown fox"

# File operations
skills-copilot file read README.md
skills-copilot file lines requirements.txt
skills-copilot file size setup.py

# System utilities
skills-copilot system info
skills-copilot system datetime-cmd
skills-copilot system set-config mykey myvalue
skills-copilot system get-config mykey
```

---

## Uninstall

If you want to uninstall:

```bash
pip uninstall skills-copilot
```

---

## Troubleshooting

### Command not found
- Make sure you installed with `pip install -e .` (editable mode)
- Check that pip's bin directory is in your PATH
- Try using `python -m src.main` instead

### Module not found errors
- Ensure you're in the project directory
- Install with: `pip install -e .`
- Check Python version: `python --version` (should be 3.8+)

### Permission denied (macOS/Linux)
- Try prefixing with `sudo`: `sudo pip install -e .`
- Or use a virtual environment (recommended)

---

## Virtual Environment Setup (Recommended)

### Create and Activate

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Install in Virtual Environment
```bash
pip install -r requirements.txt
pip install -e .
skills-copilot --help
```

### Deactivate Virtual Environment
```bash
deactivate
```

---

## Advanced: Build and Distribute

### Create a Distributable Package

```bash
# Install build tools
pip install build

# Build the package
python -m build

# This creates:
# - dist/skills_copilot-1.0.0.tar.gz (source distribution)
# - dist/skills_copilot-1.0.0-py3-none-any.whl (wheel)
```

### Install from Built Package

```bash
pip install dist/skills_copilot-1.0.0-py3-none-any.whl
```

### Publish to PyPI (Optional)

```bash
# Install twine
pip install twine

# Upload to PyPI
twine upload dist/*
```

---

## Summary

The easiest way to use this on your local system:

```bash
git clone https://github.com/Supriyo-SP/skills-copilot-codespaces-vscode.git
cd skills-copilot-codespaces-vscode
pip install -e .
skills-copilot --help
```

Then use `skills-copilot` command from anywhere on your system!
