"""Representation of a dice"""

import random


class Dice:
    """Implementation of a dice of any size"""

    def __init__(self, faces_list):
        self._faces = faces_list.copy()

    @property
    def faces(self):
        """Return all dice faces"""
        return self._faces

    @faces.setter
    def faces(self, faces_list):
        """Set dice faces according to a list"""
        self._faces = faces_list.copy()

    def roll(self):
        """Pick a random face"""
        return random.choice(self._faces)
