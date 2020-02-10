import math
import random as rd
print("Bienvenue à l'expérience immersive de IMT clicker!\nAppuyer sur Entrée pour cliquer :)")
credits_ects = 0
has_seen_morse = False
morse = r"""
               __ ___
             .'. -- . '.
            /U)  __   (O|
           /.'  ()()   '.\._
         .',/;,_.--._.;;) . '--..__
        /  ,///|.__.|.\\\  \ '.  '.''---..___
       /'._ '' ||  ||  '' _'\  :   \   '   . '.
      /        ||  ||        '.,    )   )   :  \
     :'-.__ _  ||  ||   _ __.' _\_ .'  '   '   ,)
     (          '  |'        ( __= ___..-._ ( (.\\
    ('\      .___ ___.      /'.___=          \.\.\
     \\\-..____________..-''
"""

while True:
    input()
    credits_ects+=1
    print(f"Vous avez {credits_ects} crédits ECTS!")
    if rd.randint(0,10000) == 0:
        print(morse)
        print("Vous avez trouvé un morse! Curieux.")
        if not has_seen_morse:
            print(f"Achievment unlocked : Trouver un morse")
            has_seen_morse = True
    if (math.log10(credits_ects)%1==0):
      print(f"Achievement unlocked : Obtenir {credits_ects} crédits !")
