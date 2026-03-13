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
