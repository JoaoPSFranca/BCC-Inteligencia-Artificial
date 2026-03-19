import os
import random
from os import MFD_ALLOW_SEALING

# Regras:
# Regra 1: mover o carro para a esquerda caso o objetivo esteja em uma coluna menor
# Regra 2: mover o carro para a direita caso o objetivo esteja em uma coluna maior
# Regra 3: mover o carro para a cima caso o objetivo esteja na mesma coluna
# Regra 4: caso o carro passe no objetivo, finalizar o jogo
# Regra 5: caso o carro passe pelo poder P1, mover o objetivo para a esquerda
# Regra 6: caso o carro passe pelo poder P2, mover o objetivo para a direita

priority_rules = {
    "R4": False, # Regra 4 - Prioridade 6
    "R5": False, # Regra 5 - Prioridade 5
    "R6": False, # Regra 6 - Prioridade 4
    "R3": False, # Regra 3 - Prioridade 3
    "R1": False, # Regra 1 - Prioridade 2
    "R2": False, # Regra 2 - Prioridade 1
}

class MapObject:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Car(MapObject):
    def __init__(self, col, value, turn=False):
        super().__init__(9, col)
        self.value = value
        self.turn = turn

def clear_terminal():
    # os.system('cls') # se estiver no windows
    os.system('clear') # se estiver no linux

def generate_pos_power(map, value):
    coord_powers = []
    for _ in range(3):
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if map[row][col] == 0:
                map[row][col] = value
                coord_powers.append([row, col])
                break
    return coord_powers

def generate_map():
    os.system('TERM=xterm-256color')
    map = [[0 for _ in range(10)] for _ in range(10)]
    return map

def print_map(map):
    print("." + "------." * 10)

    for row in map:
        line = "|"
        for col in row:
            if col == 0:
                char = " "
            elif col == 1:
                char = f"C1"
            elif col == 2:
                char = f"C2"
            elif col == 3:
                char = f"O"
            elif col == 4:
                char = "P1"
            elif col == 5:
                char = "P2"
            elif col == 6:
                char = "C12" # Quando os dois carros estão no mesmo quadrado

            line += f"  {char:2}  |"

        print(line)
        print("." + "------." * 10)

# Verificando Regra 1
def verify_left(car, ob):
    if car.col > ob.col:
        return True
    return False

# Verificando Regra 2
def verify_right(car, ob):
    if car.col < ob.col:
        return True
    return False

# Verificando Regra 3
def verify_up(car, ob):
    if car.row > ob.row:
        return True
    return False

# Verificando Regra 4
def verify_objective(map, ob):
    if map[ob.row][ob.col] == (1 or 2):
        return True
    return False

# Verificando Regra 5
def verify_p1(map, p1):
    for i in p1:
        if map[i[0]][i[1]] == (1 or 2):
            return True
    return False

# Verificando Regra 6
def verify_p2(map, p2):
    for i in p2:
        if map[i[0]][i[1]] == (1 or 2):
            return True
    return False

def check_rules(map, car, ob, p1, p2):
    if verify_left(car, ob):
        priority_rules["R1"] = True
    if verify_right(car, ob):
        priority_rules["R2"] = True
    if verify_up(car, ob):
        priority_rules["R3"] = True
    if verify_objective(map, ob):
        priority_rules["R4"] = True
    if verify_p1(map, p1):
        priority_rules["R5"] = True
    if verify_p2(map, p2):
        priority_rules["R6"] = True

def print_rules():
    print("Regras Válidas:")
    for key, value in priority_rules.items():
        if value:
            print(f"{key} está válida.")

def reset_rules():
    for key in priority_rules:
        priority_rules[key] = False

def choice_rule():
    for key in priority_rules:
        if priority_rules[key]:
            return key
    return None

def move_car(map, car, direction):
    if direction == "l":
        if car.col != 0:
            if map[car.row][car.col] == 6:
                if car.value == 1:
                    map[car.row][car.col] = 2
                else:
                    map[car.row][car.col] = 1
            else:
                map[car.row][car.col] = 0
            car.col -= 1
    elif direction == "r":
        if car.col != 9:
            if map[car.row][car.col] == 6:
                if car.value == 1:
                    map[car.row][car.col] = 2
                else:
                    map[car.row][car.col] = 1
            else:
                map[car.row][car.col] = 0
            car.col += 1
    elif direction == "u":
        if car.row != 0:
            if map[car.row][car.col] == 6:
                if car.value == 1:
                    map[car.row][car.col] = 2
                else:
                    map[car.row][car.col] = 1
            else: map[car.row][car.col] = 0

            car.row -= 1
            print("chegou aqui")

    if map[car.row][car.col] == (1 or 2):
        map[car.row][car.col] = 6
    else:
        map[car.row][car.col] = car.value

def move_objective(map, ob, direction):
    if direction == "l":
        if ob.col != 0:
            map[ob.row][ob.col] = 0
            ob.col -= 1
    elif direction == "r":
        if ob.col != 9:
            map[ob.row][ob.col] = 0
            ob.col += 1

    if map[ob.row][ob.col] == 1:
        map[ob.row][ob.col] = 1
    elif map[ob.row][ob.col] == 2:
        map[ob.row][ob.col] = 2
    else:
        map[ob.row][ob.col] = 3

def make_action(map, rule, car, ob, p1, p2):
    if rule == "R1":
        move_car(map, car, "l")
        print(f"Movendo C{car.value} para esquerda. ")
    elif rule == "R2":
        move_car(map, car, "r")
        print(f"Movendo C{car.value} para direita. ")
    elif rule == "R3":
        move_car(map, car, "u")
        print(f"Movendo C{car.value} para cima. ")
    elif rule == "R4":
        reset_rules()
        print(f"Objetivo alcançado, carro C{car.value} perdeu o jogo. ")
        return False
    elif rule == "R5":
        p1.remove([ob.row, ob.col])
        move_objective(map, ob, "l")
        print(f"C{car.value} passou pelo poder P1, movendo objetivo")
    elif rule == "R6":
        p2.remove([ob.row, ob.col])
        move_objective(map, ob, "r")
        print(f"C{car.value} passou pelo poder P2, movendo objetivo")

    reset_rules()
    return True

def run_game(map, c1, c2, ob, p1, p2):
    flag = True

    while flag:
        # clear_terminal()
        print_map(map)
        car = None

        if c1.turn:
            car = c1
        else:
            car = c2

        check_rules(map, car, ob, p1, p2)
        print_rules()

        rule = choice_rule()
        print(f"Regra escolhida: {rule}")

        flag = make_action(map, rule, car, ob, p1, p2)
        c1.turn = not c1.turn
        c2.turn = not c2.turn
        input("Pressione enter para continuar...")

def reset_game():
    map = generate_map()

    c1 = Car(0, 1, True)
    map[9][0] = 1
    c2 = Car(9, 2)
    map[9][9] = 2
    ob = MapObject(0, random.randint(0, 9))
    map[ob.row][ob.col] = 3
    p1 = generate_pos_power(map, 4)
    p2 = generate_pos_power(map, 5)

    run_game(map, c1, c2, ob, p1, p2)

if __name__ == "__main__":
    os.system("export TERM=xterm")
    reset_game()
