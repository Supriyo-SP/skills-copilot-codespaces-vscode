"""System information and utility commands."""
import click
import platform
import os
from pathlib import Path
from datetime import datetime
from utils import load_config, save_config


@click.group()
def system():
    """System information and utilities."""
    pass


@system.command()
def info():
    """Display system information."""
    click.echo("System Information:")
    click.echo(f"  Platform: {platform.system()} {platform.release()}")
    click.echo(f"  Python: {platform.python_version()}")
    click.echo(f"  Processor: {platform.processor()}")
    click.echo(f"  Hostname: {platform.node()}")


@system.command()
def datetime_cmd():
    """Display current date and time."""
    now = datetime.now()
    click.echo(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


@system.command()
@click.argument('key')
@click.argument('value')
def set_config(key, value):
    """Set a configuration value."""
    config = load_config()
    config[key] = value
    save_config(config)
    click.echo(f"Configuration set: {key} = {value}")


@system.command()
@click.argument('key', required=False)
def get_config(key):
    """Get configuration value(s)."""
    config = load_config()
    if key:
        if key in config:
            click.echo(f"{key} = {config[key]}")
        else:
            click.echo(f"Configuration key not found: {key}")
    else:
        if config:
            click.echo("Configuration:")
            for k, v in config.items():
                click.echo(f"  {k} = {v}")
        else:
            click.echo("No configuration set")


@system.command()
@click.argument('path', type=click.Path(exists=True))
def tree_cmd(path):
    """Display directory structure as a tree."""
    def print_tree(directory, prefix=""):
        items = sorted(Path(directory).iterdir(), key=lambda x: (not x.is_dir(), x.name))
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            current_prefix = "└── " if is_last else "├── "
            click.echo(f"{prefix}{current_prefix}{item.name}")
            if item.is_dir():
                next_prefix = prefix + ("    " if is_last else "│   ")
                print_tree(item, next_prefix)
    
    click.echo(f"{path}/")
    print_tree(path)


@system.command()
@click.argument('env_var', required=False)
def env(env_var):
    """Get environment variable(s)."""
    if env_var:
        value = os.getenv(env_var)
        if value:
            click.echo(f"{env_var} = {value}")
        else:
            click.echo(f"Environment variable not found: {env_var}")
    else:
        click.echo("Environment variables:")
        for key, value in sorted(os.environ.items()):
            click.echo(f"  {key} = {value}")
