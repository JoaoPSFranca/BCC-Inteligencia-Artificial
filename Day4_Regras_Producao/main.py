from Engine.interface import *
from Class.Villain import *
from Class.Hero import *
from Class.Persona import *
from Engine.rules import *
import os

def run_game(map, hero, villain, bonus):
    flag = True

    while flag:
        os.system("clear")
        print_map(map, villain)

        verify_rules(hero, villain, bonus)
        print_rules()

        rule = choice_rule()
        print(f"Regra escolhida: {rule}")

        flag = make_action(map, rule, hero, villain, bonus)
        input()

def reset_game():
    map = generate_map()

    villain = Villain()
    villain.move_villain(map)

    hero = Hero()
    hero.generate_hero(map)

    bonus = Persona()
    bonus.generate(map, 3)

    run_game(map, hero, villain, bonus)

if __name__ == "__main__":
    os.system("export TERM=xterm")
    reset_game()
