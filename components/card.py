""" Card Class """

class Card:
    def __init__(self, content='', points=0, dices={}, results={}):
        self.__content = content
        self.__points = points
        self.__dices = dices
        self.__results = results

    def content(self):
        return self.__content

    def points(self):
        return self.__points

    def dices(self):
        return self.__dices

    def results(self):
        return self.__results

    def show_card_info(self):
        info = {
            'content': self.__content,
            'points': self.__points,
            'dices': self.__dices,
            'results': self.__results
            }
        return info
