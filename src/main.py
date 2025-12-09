"""
Skills Copilot CLI - A fully functional command-line interface.
"""
import click
from config import APP_NAME, APP_VERSION
from commands.math_commands import math
from commands.text_commands import text
from commands.file_commands import file
from commands.system_commands import system


@click.group(invoke_without_command=True)
@click.version_option(version=APP_VERSION, prog_name=APP_NAME)
@click.pass_context
def cli(ctx):
    """
    Skills Copilot CLI - A fully functional command-line interface.
    
    Use 'skills-copilot COMMAND --help' for more information on a command.
    """
    if ctx.invoked_subcommand is None:
        click.echo(f"Welcome to {APP_NAME} v{APP_VERSION}!")
        click.echo("\nAvailable command groups:")
        click.echo("  math    - Mathematical operations")
        click.echo("  text    - Text manipulation")
        click.echo("  file    - File operations")
        click.echo("  system  - System utilities")
        click.echo("\nUse 'skills-copilot COMMAND --help' for more information.")


# Register command groups
cli.add_command(math)
cli.add_command(text)
cli.add_command(file)
cli.add_command(system)


if __name__ == "__main__":
    cli()
