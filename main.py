# -*- coding: utf-8 -*-

# Imports

import math
import random as rd
import time
import sys
from achievements import earn_unearned_achievement, milestone_names
from strings import logo, morse

# Variables

credits_ects = 0

# Intro cutscene

print("Bienvenue à l'expérience immersive de...")
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
print("\nAppuyez sur Entrée pour cliquer :)")

# Game logic

while True:
    input()
    credits_ects+=1
    print(f"Vous avez {credits_ects} crédits ECTS!")
    if rd.randint(0,999) == 0:
        print(morse)
        print("Vous avez trouvé un morse ! Curieux.")
        earn_unearned_achievement("Morse")
    if (credits_ects in milestone_names):
        earn_unearned_achievement(milestone_names[credits_ects])