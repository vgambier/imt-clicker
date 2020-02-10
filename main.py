# -*- coding: utf-8 -*-

# Imports

import math
import random as rd
import time
import sys
from achievements import earn_unearned_achievement, milestone_names, achievement_list
from strings import logo, morse

# Variables and functions

credits_ects = 0

# Intro cutscene

print("Bienvenue dans l'expérience immersive de...")
time.sleep(1)
for line in logo:
    print(line)
    time.sleep(0.5)
for c in "      ":
    sys.stdout.write(c)
    sys.stdout.flush()
for c in "C L I C K E R":
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.25)
time.sleep(1)
print("\nAppuyez sur Entrée pour cliquer. Tapez help pour une liste de commandes.")

# Game logic

while True:

    user_input = "default"
    while user_input != "":
        user_input = input("> ")
        if user_input == "help":
            print('''List of commands:\n\thelp: display this message\n\tachievements: view achievements''')
        elif user_input == "achievements":
            print([key if achievement_list[key] else "???" for key in achievement_list])
        elif user_input == "click":
            print("Nan, pour cliquer faut juste faire entrée sans rien écrire")
        elif user_input != "":
            print("Invalid command. Did you mean \"click\"?")

    credits_ects += 1
    print(f"Vous avez {credits_ects} crédits ECTS!")

    if rd.randint(0, 999) == 0:
        print(morse)
        print("Vous avez trouvé un morse ! Curieux.")
        earn_unearned_achievement("Morse")

    if credits_ects in milestone_names:
        earn_unearned_achievement(milestone_names[credits_ects])
