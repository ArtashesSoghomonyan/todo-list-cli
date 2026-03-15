import os
import json
import argparse

from todolist import TodoList
from utils import clear_the_console, green, red


SOURCE = os.path.expanduser('~/.todo.json')

EMPTY_JSON_FORM = """{
  "items": []
}
"""


def main():
    clear_the_console()

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--list", "-l", help="Show all of the todos.", required=False, action="store_true")
    argument_parser.add_argument("--add", "-a", help="Add a new todo", required=False, type=str)
    argument_parser.add_argument("--remove", "-r", help="Remove todo from list by number", required=False, type=int)
    argument_parser.add_argument("--check", "-c", help="Mark item as complete (done)", required=False, type=int)
    argument_parser.add_argument("--uncheck", "-u", help="Mark item as incomplete (undone)", required=False, type=int)
    arguments = argument_parser.parse_args()

    try:
        with open(SOURCE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open(SOURCE, "w") as file:
            file.write(EMPTY_JSON_FORM)
            data = json.loads(EMPTY_JSON_FORM)

    if "items" in data.keys():
        todos = TodoList(data["items"])
    else:
        todos = TodoList([])

    if arguments.list:
        print(todos)
    elif arguments.add:
        green(f"+++ added a new note: {arguments.add}\n")
        todos.add_item(arguments.add)
        print(todos)
    elif arguments.remove:
        if arguments.remove <= len(todos.items) and arguments.remove > 0:
            red(f"--- removed note: {todos.items[arguments.remove - 1]["name"]}\n")
        todos.remove_item(arguments.remove - 1)
        print(todos)
    elif arguments.check:
        if arguments.check <= len(todos.items) and arguments.check > 0:
            print(f"xxx checked note: {todos.items[arguments.check - 1]["name"]} \n")
        todos.check_item(arguments.check - 1)
        print(todos)
    elif arguments.uncheck:
        if arguments.uncheck <= len(todos.items) and arguments.uncheck > 0:
            print(f"[ ] unchecked note: {todos.items[arguments.uncheck - 1]["name"]} \n")
        todos.check_item(arguments.uncheck - 1)
        print(todos)
    else:
        print("Todo list cli: use -h or --help flag for more information")

    # Save the result
    with open(SOURCE, 'w') as file:
        result = {
            "items": todos.items,
        }
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    main()
