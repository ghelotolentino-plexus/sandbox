import typer

app = typer.Typer()


@app.command()
def hello():
    """Print Hello World."""
    typer.echo("Hello World")
