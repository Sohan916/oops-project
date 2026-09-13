from card import Card
from utils import new_id


class List:
    def __init__(self, name) -> None:
        self.id = new_id()
        self.name = name
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, cardId: str):
        card = self.find_card(cardId)
        self.cards.remove(card)

    def find_card(self, cardId: str):
        for card in self.cards:
            if card.id == cardId:
                return card
        return None
