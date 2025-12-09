.PHONY: help install install-dev test test-cov run clean lint format

help:
	@echo "Skills Copilot CLI - Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make install-dev  - Install dependencies with dev tools"
	@echo "  make test         - Run tests"
	@echo "  make test-cov     - Run tests with coverage report"
	@echo "  make run          - Run the CLI"
	@echo "  make clean        - Clean up generated files"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install pytest-cov pylint black

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=src --cov-report=term-missing

run:
	python -m src.main

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf build dist *.egg-info
	rm -rf .coverage htmlcov
	@echo "Cleanup complete!"

lint:
	pylint src/ || true

format:
	black src/ tests/
