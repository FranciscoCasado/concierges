"""Representation of a deck of cards"""
import random
class Deck:
    """Representation of a deck of cards of any size, as a stack"""
    def __init__(self, card_pile):
        """Create deck by copying a list of cards given in parameter card_pile"""
        self._cards = card_pile.copy()

    def draw_card(self):
        """Pick the element at the top of the stack"""
        return self._cards.pop()

    def put_card_on_top(self, card):
        """Put card at the top of the stack"""
        self._cards.append(card)

    def put_card_in_middle(self, card):
        """Put card at a random place in the stack"""
        index = random.randint(0,len(self._cards))
        self._cards.insert(index, card)
