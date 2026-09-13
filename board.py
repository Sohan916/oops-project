from list import List


class Board:
    def __init__(self) -> None:
        self.Lists = []

    # List methods.
    def add_list(self, name):
        self.Lists.append(List(name))

    def remove_list(self, list_id):
        list = self.find_list(list_id)
        if list is None:
            raise ValueError("invalid value")
        self.Lists.remove(list)

    def find_list(self, list_id) -> List | None:
        for list in self.Lists:
            if list_id == list.id:
                return list

