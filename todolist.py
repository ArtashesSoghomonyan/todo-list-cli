from typing import TypedDict

from utils import user_error, yes_no_prompt, warning


class Todo(TypedDict):
    # After changing this TypedDict also change the todo validation function
    name: str
    done: bool


class TodoList:
    def __init__(self, items: list[Todo]) -> None:
        # Check for validation
        valid_items = [item for item in items if self.is_valid_todo(item)]
        self.items: list[Todo] = valid_items

    def __str__(self) -> str:
        result: str = ""

        for index, item in enumerate(self.items):
            if item["done"]:
                result += f"{index + 1}. ✅ {item["name"]}"
            else:
                result += f"{index + 1}. ⬜ {item["name"]}"

            if index != len(self.items) - 1:
                result += "\n"

        return result

    def add_item(self, name: str) -> None:
        if name in [item["name"] for item in self.items]:
            answer = yes_no_prompt(warning(f"A task with name \"{name}\" already exists, would you still like to create another one?"))

            if answer == "No":
                return None

        self.items.append({
            "name": name,
            "done": False,
        })

    def remove_item(self, index: int) -> None:
        if index >= len(self.items) or index < 0:
            user_error(f"There is no item No:{index + 1}")
        else:
            del self.items[index]

    def check_item(self, index: int) -> None:
        if index >= len(self.items) or index < 0:
            user_error(f"There is no item No:{index + 1}")
        else:
            self.items[index]["done"] = True

    def uncheck_item(self, index: int) -> None:
        if index >= len(self.items) or index < 0:
            user_error(f"There is no item No:{index + 1}")
        else:
            self.items[index]["done"] = False

    @staticmethod
    def is_valid_todo(todo: object) -> bool:
        valid_keys = ["name", "done"]
        valid_value_types = [str, bool]

        if not isinstance(todo, dict):
            return False

        if len([x for x in todo.keys() if x not in valid_keys]) != 0:
            return False
        elif [type(x) for x in todo.values()] != valid_value_types:
            return False
        return True
