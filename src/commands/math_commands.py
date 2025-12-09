"""Mathematical operations commands."""
import click
import math


@click.group()
def math():
    """Mathematical operations."""
    pass


@math.command()
@click.argument('numbers', nargs=-1, type=float, required=True)
def add(numbers):
    """Add numbers together."""
    result = sum(numbers)
    click.echo(f"Result: {result}")


@math.command()
@click.argument('numbers', nargs=-1, type=float, required=True)
def multiply(numbers):
    """Multiply numbers together."""
    result = 1
    for num in numbers:
        result *= num
    click.echo(f"Result: {result}")


@math.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def subtract(a, b):
    """Subtract b from a."""
    result = a - b
    click.echo(f"Result: {result}")


@math.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def divide(a, b):
    """Divide a by b."""
    if b == 0:
        click.echo("Error: Cannot divide by zero!")
        return
    result = a / b
    click.echo(f"Result: {result}")


@math.command()
@click.argument('n', type=int)
def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        click.echo("Error: Factorial is not defined for negative numbers!")
        return
    result = math.factorial(n)
    click.echo(f"{n}! = {result}")


@math.command()
@click.argument('n', type=float)
def sqrt(n):
    """Calculate square root of n."""
    if n < 0:
        click.echo("Error: Cannot calculate square root of negative number!")
        return
    result = math.sqrt(n)
    click.echo(f"√{n} = {result}")
