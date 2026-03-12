import platform
import subprocess


def clear_the_console():
    if platform.system() == "Windows":
        subprocess.run("cls")
    else:  # Assumes Linux/macOS/Unix
        subprocess.run("clear")
