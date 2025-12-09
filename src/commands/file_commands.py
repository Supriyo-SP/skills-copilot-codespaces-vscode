"""File operations commands."""
import click
from pathlib import Path
from utils import read_file, write_file, load_json_file, save_json_file


@click.group()
def file():
    """File operations."""
    pass


@file.command()
@click.argument('file_path', type=click.Path(exists=True))
def read(file_path):
    """Read and display file contents."""
    try:
        content = read_file(file_path)
        click.echo(content)
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)


@file.command()
@click.argument('file_path')
@click.argument('content')
def write(file_path, content):
    """Write content to a file."""
    try:
        write_file(file_path, content)
        click.echo(f"File written successfully: {file_path}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@file.command()
@click.argument('file_path', type=click.Path(exists=True))
def lines(file_path):
    """Count lines in a file."""
    try:
        content = read_file(file_path)
        line_count = len(content.splitlines())
        click.echo(f"Line count: {line_count}")
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)


@file.command()
@click.argument('file_path', type=click.Path(exists=True))
def size(file_path):
    """Get file size in bytes."""
    try:
        size_bytes = Path(file_path).stat().st_size
        click.echo(f"File size: {size_bytes} bytes")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@file.command()
@click.argument('file_path', type=click.Path(exists=True))
def exists_cmd(file_path):
    """Check if a file exists."""
    if Path(file_path).exists():
        click.echo(f"File exists: {file_path}")
    else:
        click.echo(f"File does not exist: {file_path}")


@file.command()
@click.argument('json_file', type=click.Path(exists=True))
def read_json(json_file):
    """Read and display JSON file contents."""
    try:
        data = load_json_file(json_file)
        import json
        click.echo(json.dumps(data, indent=2))
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@file.command()
@click.argument('json_file')
@click.argument('json_data')
def write_json(json_file, json_data):
    """Write JSON data to a file."""
    try:
        import json
        data = json.loads(json_data)
        save_json_file(json_file, data)
        click.echo(f"JSON file written successfully: {json_file}")
    except json.JSONDecodeError:
        click.echo("Error: Invalid JSON data", err=True)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
