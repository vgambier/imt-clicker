# -*- coding: utf-8 -*-

# Imports
import math
import random as rd
import time
import sys

# Variables and functions
from strings import logo, morse

credits_ects = 0

achievements = dict()
achievements["Morse"] = False

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
    if rd.randint(0,1) == 0:
        print(morse)
        print("Vous avez trouvé un morse! Curieux.")
        if not achievements["Morse"]:
            print("Achievment unlocked : Trouver un morse")
            achievements["Morse"] = True
    if (math.log10(credits_ects)%1==0):
      print(f"Achievement unlocked : Obtenir {credits_ects} crédits !")
