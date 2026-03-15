from typing import TypedDict

from utils import user_error


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

    def clear(self) -> None:
        self.items = []

    def is_unique_item(self, name: str) -> bool:
        return name in [item["name"] for item in self.items]

    @staticmethod
    def is_valid_todo(todo: object) -> bool:
        valid_keys = {"name", "done"}

        return (
            isinstance(todo, dict) and
            set(todo.keys()) == valid_keys and
            isinstance(todo.get('name'), str) and
            isinstance(todo.get('done'), bool)
        )
