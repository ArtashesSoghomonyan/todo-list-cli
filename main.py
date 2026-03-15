import os
import json
import argparse
import tomllib
from pathlib import Path

from todolist import TodoList
from utils import green, red, warning, yes_no_prompt


SOURCE = os.path.expanduser("~/.todo.json")

with open(Path(__file__).parent / "pyproject.toml", "rb") as f:
    VERSION = tomllib.load(f)["project"]["version"]

EMPTY_JSON_FORM = """{
  "items": []
}
"""

def load_todos(source: str) -> TodoList:
    try:
        with open(source, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open(source, "w") as file:
            file.write(EMPTY_JSON_FORM)
            data = json.loads(EMPTY_JSON_FORM)

    if "items" in data.keys():
        todos = TodoList(data["items"])
    else:
        todos = TodoList([])

    return todos


def main() -> None:
    # clear_the_console()

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--list", "-l", help="Show all of the todos.", required=False, action="store_true")
    argument_parser.add_argument("--version", "-v", action="version", version=f"v{VERSION}")
    argument_parser.add_argument("--clear", help="Remove every task/todo", required=False, action="store_true")
    argument_parser.add_argument("--add", "-a", help="Add a new todo", required=False, type=str)
    argument_parser.add_argument("--remove", "-r", help="Remove todo from list by number", required=False, type=int)
    argument_parser.add_argument("--check", "-c", help="Mark item as complete (done)", required=False, type=int)
    argument_parser.add_argument("--uncheck", "-u", help="Mark item as incomplete (undone)", required=False, type=int)
    arguments = argument_parser.parse_args()

    todos = load_todos(SOURCE)

    if arguments.list:
        if len(todos.items) == 0:
            print("You have no tasks to do. Use --add to add some")
        else:
            print(todos)
    elif arguments.add:
        if not todos.is_unique_item(arguments.add):
            answer = yes_no_prompt(warning(f"A task with name \"{arguments.add}\" already exists, would you still like to create another one?"))
            if answer == "No":
                return None

        print(green(f"+++ added a new note: {arguments.add}\n"))
        todos.add_item(arguments.add)
        print(todos)
    elif arguments.remove:
        if arguments.remove <= len(todos.items) and arguments.remove > 0:
            print(red(f"--- removed note: {todos.items[arguments.remove - 1]["name"]}\n"))
        todos.remove_item(arguments.remove - 1)
        print(todos)
    elif arguments.check:
        if arguments.check <= len(todos.items) and arguments.check > 0:
            print(green(f"[x] checked note: {todos.items[arguments.check - 1]["name"]} \n"))
        todos.check_item(arguments.check - 1)
        print(todos)
    elif arguments.uncheck:
        if arguments.uncheck <= len(todos.items) and arguments.uncheck > 0:
            print(red(f"[ ] unchecked note: {todos.items[arguments.uncheck - 1]["name"]} \n"))
        todos.uncheck_item(arguments.uncheck - 1)
        print(todos)
    elif arguments.clear:
        answer = yes_no_prompt(warning("Are you sure that you want to delete ALL of your tasks?"))

        if answer == "No":
            return None
        else:
            todos.clear()
            print("You have deleted all of your tasks.")
    else:
        print(f"Todo list cli v{VERSION}: use -h or --help flag for more information")

    # Save the result
    with open(SOURCE, 'w') as file:
        result = {
            "items": todos.items,
        }
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    main()
