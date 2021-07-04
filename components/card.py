""" Card Class """

class Card:
    def __init__(self, content='', points=0, dices={}, results={}):
        self._content = content
        self._points = points
        self._dices = dices
        self._results = results

    @property()
    def content(self):
        return self._content

    @property()
    def points(self):
        return self._points

    @property()
    def dices(self):
        return self._dices

    @property()
    def results(self):
        return self._results

    def show_card_info(self):
        info = {
            'content': self.content,
            'points': self.points,
            'dices': self.dices,
            'results': self.results
            }
        return info
