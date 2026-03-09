from Class.Persona import Persona

class Hero(Persona):
    def __init__(self):
        super().__init__()
        self.dmg = 1

    def generate_hero(self, map):
        self.generate(map, 2)

    def move_hero(self, map, direction):
        new_row, new_col = self.row, self.col

        if direction == "u":
            new_row -= 1
        elif direction == "d":
            new_row += 1
        elif direction == "l":
            new_col -= 1
        elif direction == "r":
            new_col += 1

        if 0 <= new_row < 10 and 0 <= new_col < 10:
            map[self.row][self.col] = 0
            self.row, self.col = new_row, new_col

            if map[new_row][new_col] == 3:
                map[self.row][self.col] = 5
            elif map[new_row][new_col] == 1:
                map[self.row][self.col] = 4
            else:
                map[self.row][self.col] = 2

    def attack(self, map, villain):
        if self.row == villain.row and self.col == villain.col:
            villain.lose_life(map, self.dmg)
            return True
        print("Coordenada errada")
        return False

    def pick_bonus(self, map):
        if map[self.row][self.col] == 5:
            self.dmg += 1
            map[self.row][self.col] = 2
            return True

        return False