# Skills Copilot CLI

A fully functional, production-ready command-line interface built with Python and Click.

## Features

- **Math Operations**: Add, multiply, subtract, divide, factorial, square root
- **Text Manipulation**: Uppercase, lowercase, reverse, capitalize, word/char count, replace
- **File Operations**: Read, write, count lines, check file size, JSON handling
- **System Utilities**: System info, datetime, configuration management, directory tree, environment variables

## Installation

```bash
# Install dependencies
make install

# Or install with dev tools
make install-dev
```

## Usage

### Basic Commands

```bash
# Display help
python -m src.main --help

# Check version
python -m src.main --version

# View welcome message
python -m src.main
```

### Math Operations

```bash
# Add numbers
python -m src.main math add 10 20 30

# Multiply
python -m src.main math multiply 5 4

# Subtract
python -m src.main math subtract 100 30

# Divide
python -m src.main math divide 100 5

# Factorial
python -m src.main math factorial 5

# Square root
python -m src.main math sqrt 16
```

### Text Operations

```bash
# Convert to uppercase
python -m src.main text uppercase hello

# Convert to lowercase
python -m src.main text lowercase HELLO

# Reverse text
python -m src.main text reverse "hello world"

# Capitalize
python -m src.main text capitalize "hello world"

# Count words
python -m src.main text word-count "hello world test"

# Count characters
python -m src.main text char-count "hello"

# Replace text
python -m src.main text replace "hello world" "world" "universe"
```

### File Operations

```bash
# Read file
python -m src.main file read myfile.txt

# Write to file
python -m src.main file write myfile.txt "Hello, World!"

# Count lines
python -m src.main file lines myfile.txt

# Get file size
python -m src.main file size myfile.txt

# Check if file exists
python -m src.main file exists-cmd myfile.txt

# Read JSON
python -m src.main file read-json config.json

# Write JSON
python -m src.main file write-json config.json '{"name": "John", "age": 30}'
```

### System Operations

```bash
# System information
python -m src.main system info

# Current date and time
python -m src.main system datetime-cmd

# Set configuration
python -m src.main system set-config mykey myvalue

# Get configuration
python -m src.main system get-config mykey

# Get all configuration
python -m src.main system get-config

# Display directory tree
python -m src.main system tree-cmd .

# Get environment variable
python -m src.main system env PATH

# List all environment variables
python -m src.main system env
```

## Testing

```bash
# Run tests
make test

# Run tests with coverage
make test-cov

# Clean build artifacts
make clean
```

## Project Structure

```
skills-copilot/
├── src/
│   ├── main.py              # Main CLI entry point
│   ├── config.py            # Configuration and constants
│   ├── utils.py             # Utility functions
│   └── commands/
│       ├── __init__.py
│       ├── math_commands.py      # Math operations
│       ├── text_commands.py      # Text operations
│       ├── file_commands.py      # File operations
│       └── system_commands.py    # System utilities
├── tests/
│   └── test_main.py         # Test suite
├── requirements.txt         # Project dependencies
├── setup.py                 # Package configuration
├── Makefile                 # Build commands
└── README.md                # This file
```

## Development

### Install Development Dependencies

```bash
make install-dev
```

### Run with Make

```bash
make run          # Run the CLI
make test         # Run tests
make test-cov     # Run tests with coverage
make clean        # Clean up
```

## Requirements

- Python 3.8+
- Click 8.1.7+
- pytest 7.4.3+ (for testing)

## License

MIT
