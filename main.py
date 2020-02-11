# -*- coding: utf-8 -*-

# Imports

import math
import random as rd
import time
import sys
from achievements import earn_unearned_achievement, milestone_names
from strings import logo, morse
from pynput import keyboard








class Game :

    # Variables
    def __init__(self):
        self.credits_ects = 0
        self.enter_pressed = False
        self.game_over = False
        #self.play_intro()
        self.start_game()

    def on_release(self, key):
        if key == keyboard.Key.enter:
            self.credits_ects += 1
            print(f"Vous avez {self.credits_ects} crédits ECTS!")
            if rd.randint(0, 999) == 0:
                print(morse)
                print("Vous avez trouvé un morse ! Curieux.")
                earn_unearned_achievement("Morse")
            if (self.credits_ects in milestone_names):
                earn_unearned_achievement(milestone_names[self.credits_ects])
        if key == keyboard.Key.esc:  #exit game
            self.game_over = True
            return False



    def play_intro(self):
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
    def start_game(self):
        listener = keyboard.Listener(

            on_release=self.on_release)
        listener.start()
        while not self.game_over:
            pass
        print("Game finished!")




if __name__ == '__main__':
    Game()