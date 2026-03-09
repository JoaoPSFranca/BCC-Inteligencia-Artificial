import random
import os
from Class.Colors import *

def clear_terminal():
    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    os.system('clear')

def generate_map():
    os.system('TERM=xterm-256color')
    map = [[0 for _ in range(10)] for _ in range(10)]
    return map

def print_map(map, villain):
    print("." + "---." * 10)

    for row in map:
        line = "|"
        for col in row:
            if col == 0:
                char = " "
            elif col == 1:
                char = f"{villain.color}V{Color.RESET}"
            elif col == 2:
                char = f"{Color.BLUE}H{Color.RESET}"
            elif col == 3:
                char = f"{Color.CYAN}B{Color.RESET}"
            elif col == 4:
                char = "VH"
            elif col == 5:
                char = "BH"

            line += f" {char} |"

        print(line)
        print("." + "---." * 10)
