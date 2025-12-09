"""Text manipulation commands."""
import click


@click.group()
def text():
    """Text manipulation operations."""
    pass


@text.command()
@click.argument('text')
def uppercase(text):
    """Convert text to uppercase."""
    click.echo(text.upper())


@text.command()
@click.argument('text')
def lowercase(text):
    """Convert text to lowercase."""
    click.echo(text.lower())


@text.command()
@click.argument('text')
def reverse(text):
    """Reverse text."""
    click.echo(text[::-1])


@text.command()
@click.argument('text')
def capitalize(text):
    """Capitalize first letter of each word."""
    click.echo(text.title())


@text.command()
@click.argument('text')
def word_count(text):
    """Count words in text."""
    words = text.split()
    click.echo(f"Word count: {len(words)}")


@text.command()
@click.argument('text')
def char_count(text):
    """Count characters in text."""
    click.echo(f"Character count: {len(text)}")


@text.command()
@click.argument('text')
@click.argument('old', required=True)
@click.argument('new', required=True)
def replace(text, old, new):
    """Replace occurrences of old with new in text."""
    result = text.replace(old, new)
    click.echo(result)
