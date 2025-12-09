"""Tests for the CLI module."""
import sys
import os
from click.testing import CliRunner

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import cli


class TestMathCommands:
    """Test math command group."""
    
    def test_add(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['math', 'add', '5', '3'])
        assert result.exit_code == 0
        assert "Result: 8" in result.output
    
    def test_multiply(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['math', 'multiply', '4', '5'])
        assert result.exit_code == 0
        assert "Result: 20" in result.output
    
    def test_sqrt(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['math', 'sqrt', '16'])
        assert result.exit_code == 0
        assert "4.0" in result.output


class TestTextCommands:
    """Test text command group."""
    
    def test_uppercase(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['text', 'uppercase', 'hello'])
        assert result.exit_code == 0
        assert "HELLO" in result.output
    
    def test_lowercase(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['text', 'lowercase', 'HELLO'])
        assert result.exit_code == 0
        assert "hello" in result.output
    
    def test_reverse(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['text', 'reverse', 'hello'])
        assert result.exit_code == 0
        assert "olleh" in result.output
    
    def test_word_count(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['text', 'word-count', 'hello world test'])
        assert result.exit_code == 0
        assert "Word count: 3" in result.output


class TestCLI:
    """Test main CLI functionality."""
    
    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['--help'])
        assert result.exit_code == 0
        assert "Skills Copilot CLI" in result.output
    
    def test_cli_version(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['--version'])
        assert result.exit_code == 0
        assert "1.0.0" in result.output
    
    def test_cli_no_command(self):
        runner = CliRunner()
        result = runner.invoke(cli, [])
        assert result.exit_code == 0
        assert "Welcome to Skills Copilot CLI" in result.output
