from typing import TypedDict


class Todo(TypedDict):
    name: str
    done: bool


class TodoList:
    def __init__(self, items: list[Todo]) -> None:
        self.items = items

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
            raise IndexError(f"There is no item No:{index + 1}")
        else:
            del self.items[index]

    def check_item(self, index: int) -> None:
        if index >= len(self.items) or index < 0:
            raise IndexError(f"There is no item No:{index + 1}")
        else:
            self.items[index]["done"] = True

    def uncheck_item(self, index: int) -> None:
        if index >= len(self.items) or index < 0:
            raise IndexError(f"There is no item No:{index + 1}")
        else:
            self.items[index]["done"] = False
