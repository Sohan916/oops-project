from list import List


class Board:
    def __init__(self) -> None:
        self.Lists = []

    def add_list(self):

        self.Lists.append(List())
