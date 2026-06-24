import importlib
import pkgutil
from pathlib import Path

import typer


def load_commands(app: typer.Typer):
    """Discover and register all commands from apps/*/commands/* modules."""
    apps_dir = Path(__file__).parent.parent

    for app_path in sorted(apps_dir.iterdir()):
        if not app_path.is_dir() or app_path.name.startswith("_"):
            continue

        commands_dir = app_path / "commands"
        if not commands_dir.is_dir():
            continue

        for module_info in pkgutil.iter_modules([str(commands_dir)]):
            module_name = f"apps.{app_path.name}.commands.{module_info.name}"
            module = importlib.import_module(module_name)

            if hasattr(module, "app"):
                app.add_typer(module.app, name=module_info.name)
