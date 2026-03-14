import platform
import subprocess
import sys

from rich import print as rprint


def clear_the_console() -> None:
    if platform.system() == "Windows":
        subprocess.run("cls")
    else:  # Assumes Linux/macOS/Unix
        subprocess.run("clear")


def user_error(message: str):
    rprint(f"[bold red]error: {message}[/bold red]")
    sys.exit(1)


def is_valid_todo(todo: dict) -> bool:
    valid_keys = ["name", "done"]
    valid_value_types = [str, bool]

    if not isinstance(todo, dict):
        return False

    if len([x for x in todo.keys() if x not in valid_keys]) != 0:
        return False
    elif [type(x) for x in todo.values()] != valid_value_types:
       return False
    return True
