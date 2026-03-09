priority_rules = {
    "R7": False,
    "R8": False,
    "R6": False,
    "R1": False,
    "R9": False,
    "R5": False,
    "R2": False,
    "R3": False,
    "R4": False,
}

def dist_villain(hero, villain):    
    dist = abs((villain.row - hero.row)) + abs((villain.col - hero.col))
    return dist

def dist_bonus(hero, bonus):
    dist = abs((bonus.row - hero.row)) + abs((hero.col - bonus.col))
    return dist

def verify_dist_villain_bonus(hero, villain, bonus):
    if dist_villain(hero, villain) > dist_bonus(hero, bonus) and bonus.available:
        return True
    return False

def verify_hero_villain(hero, villain):
    if hero.row == villain.row and hero.col == villain.col:
        return True
    return False

def verify_left(hero, villain, bonus):
    if verify_dist_villain_bonus(hero, villain, bonus):
        if hero.col > bonus.col:
            return True
    elif hero.col > villain.col:
        return True
    return False

def verify_right(hero, villain, bonus):
    if verify_dist_villain_bonus(hero, villain, bonus):
        if hero.col < bonus.col:
            return True
    elif hero.col < villain.col:
        return True
    return False

def verify_up(hero, villain, bonus):
    if verify_dist_villain_bonus(hero, villain, bonus):
        if hero.row > bonus.row:
            return True
    elif hero.row > villain.row:
        return True
    return False

def verify_down(hero, villain, bonus):
    if verify_dist_villain_bonus(hero, villain, bonus):
        if hero.row < bonus.row:
            return True
    elif hero.row < villain.row:
        return True
    return False

def verify_hero_villain_bonus(hero, villain):
    if verify_hero_villain(hero, villain) and hero.dmg == 2:
        return True
    return False

def verify_villain_hero_death(hero, villain):
    if verify_hero_villain(hero, villain) and villain.life <= 0:
        return True
    return False

def verify_villain_life(villain):
    if villain.previous_life > villain.life:
        return True
    return False

def verify_hero_bonus(hero, bonus):
    if hero.row == bonus.row and hero.col == bonus.col and bonus.available:
        return True
    return False

def verify_rules(hero, villain, bonus):
    if verify_hero_villain(hero, villain):
        priority_rules["R1"] = True
    if verify_left(hero, villain, bonus):
        priority_rules["R2"] = True
    if verify_right(hero, villain, bonus):
        priority_rules["R3"] = True
    if verify_down(hero, villain, bonus):
        priority_rules["R4"] = True
    if verify_up(hero, villain, bonus):
        priority_rules["R5"] = True
    if verify_hero_villain_bonus(hero, villain):
        priority_rules["R6"] = True
    if verify_villain_hero_death(hero, villain):
        priority_rules["R7"] = True
    if verify_villain_life(villain):
        priority_rules["R8"] = True
    if verify_hero_bonus(hero, bonus):
        priority_rules["R9"] = True

def print_rules():
    print("Regras Válidas:")
    for key, value in priority_rules.items():
        if value:
            print(f"{key} está Válida.")

def choice_rule():
    for key in priority_rules:
        if priority_rules[key]:
            return key
    return None

def reset_rules():
    for key in priority_rules:
        priority_rules[key] = False

def make_action(map, rule, hero, villain, bonus):
    if rule == "R1":
        hero.attack(map, villain)
        print("Atacando Vilão ")
    elif rule == "R2":
        hero.move_hero(map, "l")
        print("Indo para a Esquerda")
    elif rule == "R3":
        hero.move_hero(map, "r")
        print("Indo para a Direita")
    elif rule == "R4":
        hero.move_hero(map, "d")
        print("Indo para a Baixo")
    elif rule == "R5":
        hero.move_hero(map, "u")
        print("Indo para a Cima")
    elif rule == "R6":
        villain.lose_life(map, hero.dmg)
        hero.dmg = 1
        print("Atacando vilão com o Bonus")
    elif rule == "R7":
        reset_rules()
        print("Vilão Morto, acabou o jogo!")
        return False
    elif rule == "R8":
        villain.move_villain(map)
        map[hero.row][hero.col] = 2
        print("Vilão ferido, movendo de lugar")
    elif rule == "R9":
        hero.pick_bonus(map)
        bonus.available = False
        print("Pegando Bônus")

    reset_rules()
    return True
