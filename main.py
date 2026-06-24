import typer

from apps.shared.load_commands import load_commands

app = typer.Typer()

load_commands(app)

if __name__ == "__main__":
    app()
