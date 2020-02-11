# -*- coding: utf-8 -*-

# Imports
import math
import random as rd
import time
import sys

from pynput.keyboard import KeyCode

from achievements import earn_unearned_achievement, milestone_names, achievement_list
from strings import logo, morse
from pynput import keyboard


# Intro cutscene
def play_intro():

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
    print("\nAppuyez sur Entrée pour cliquer, et sur \"h\" pour une liste des commandes :)")


class Game:

    def __init__(self):
        # Variables
        self.credits_ects = 0
        self.enter_pressed = False
        self.game_over = False

        play_intro()
        self.start_game()

    def on_release(self, key):

        if key == keyboard.Key.enter: # click

            self.credits_ects += 1
            print(f"Vous avez {self.credits_ects} crédits ECTS!")

            if rd.randint(0, 999) == 0:
                print(morse)
                print("Vous avez trouvé un morse ! Curieux.")
                earn_unearned_achievement("Morse")

            if self.credits_ects in milestone_names:
                earn_unearned_achievement(milestone_names[self.credits_ects])

        elif key == KeyCode.from_char('a'):
            print("List of achievements:")
            print([key if achievement_list[key] else "???" for key in achievement_list])

        elif key == KeyCode.from_char('h'):
            print('''List of commands:
        h (help): display this message
        a (achievements): view achievements
        Enter: click
        Esc: quit game''')

        elif key == KeyCode.from_char('c'):
            print("Nan, pour cliquer faut juste faire entrée sans rien écrire")

        elif key == keyboard.Key.esc:  # exit game
            self.game_over = True
            return False

        else:
            print("Invalid command. Did you mean \"c\" (click)?")

    # Game logic
    def start_game(self):
        listener = keyboard.Listener(on_release=self.on_release)
        listener.start()
        while not self.game_over:
            pass
        print("Game finished!")


if __name__ == '__main__':
    Game()
