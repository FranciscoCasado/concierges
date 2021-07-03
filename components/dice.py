import random

class Dice:
    def __init__(self, faces_list):
        self.faces = [0]
        self.__set_faces(faces_list)

    def __set_faces(self, faces_list):
        if not isinstance(faces_list, list):
            raise TypeError("Las caras deben ser listas")

        if not faces_list:
            raise ValueError("El dado debe tener al menos una cara")

        self.faces = faces_list.copy()

    def roll(self):
        return random.choice(self.faces)
