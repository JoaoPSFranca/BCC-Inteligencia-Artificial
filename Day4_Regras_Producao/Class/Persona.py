import random

class Persona:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
        self.available = True

    def generate(self, map, value):
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if map[row][col] == 0:
                map[row][col] = value
                self.row = row
                self.col = col
                break