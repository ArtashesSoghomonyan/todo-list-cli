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
                result += f"{index + 1}) [x] {item["name"]}"
            else:
                result += f"{index + 1}) [ ] {item["name"]}"

            if index != len(self.items) - 1:
                result += "\n"

        return result

    def add_item(self, item: Todo):
        self.items.append(item)

    def remove_item(self, index: int):
        if index >= len(self.items):
            raise IndexError(f"There is no item No:{index + 1}")
        else:
            del self.items[index]
