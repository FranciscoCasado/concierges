import random
class Deck:
    def __init__(self, card_pile):
        self.__cards = []
        self.__build(card_pile)

    def __build(self, card_pile):
        if not isinstance(card_pile, list):
            raise TypeError("La pila de cartas debe ser una lista")

        if not card_pile:
            raise ValueError("La pila de tener al menos una carta")

        self.__cards = card_pile.copy()

    def draw_card(self):
        return self.__cards.pop()

    def put_card_on_top(self, card):
        self.__cards.append(card)

    def put_card_in_middle(self, card):
        index = random.randint(0,len(self.__cards))
        self.__cards.insert(index, card)

