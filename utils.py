import platform
import subprocess
import sys
from typing import Never

import inquirer


# Colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m" # No color


def clear_the_console() -> None:
    if platform.system() == "Windows":
        subprocess.run("cls")
    else:  # Assumes Linux/macOS/Unix
        subprocess.run("clear")


def user_error(message: str) -> Never:
    print(f"{RED}error: {message}{NC}")
    sys.exit(1)


def warning(message: str) -> str:
    return f"{YELLOW}[warn]: {message}{NC}"


def info(message: str) -> str:
    return f"{BLUE}[info]: {message}{NC}"


def green(message: str) -> str:
    return f"{GREEN}{message}{NC}"


def red(message: str) -> str:
    return f"{RED}{message}{NC}"


def yes_no_prompt(message: str) -> str:
    answer = inquirer.prompt([inquirer.List(
            "value",
            message=message,
            choices=["Yes", "No"],
        )])

    if answer is None:
        sys.exit(1)
    else:
        return answer["value"]
