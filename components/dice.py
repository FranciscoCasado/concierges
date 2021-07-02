import random

class Dice:
    def __init__(self, faces):
        if not isinstance(faces, list):
            raise TypeError("Las caras deben ser listas")
        
        self.face_count = len(faces)
        if (self.face_count == 0):
            raise ValueError("El dado debe tener al menos una cara")

        self.faces = faces.copy()
        

    def roll(self):
        result = random.randint(0, self.face_count-1)
        return self.faces[result]



    