from Class.Colors import *
from Class.Persona import *

class Villain(Persona):
    def __init__(self):
        super().__init__()
        self.previous_life = 3
        self.life = 3
        self.color = Color.GREEN

    def move_villain(self, map):
        self.generate(map, 1)
        self.previous_life = self.life

    def lose_life(self, map, dmg):
        self.previous_life = self.life
        self.life -= dmg

        if self.life > 0:
            if self.life == 2:
                self.color = Color.YELLOW
            elif self.life == 1:
                self.color = Color.RED
        else:
            self.life = 0
