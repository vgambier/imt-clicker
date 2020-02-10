import math
print("Bienvenue à l'expérience immersive de IMT clicker!\nAppuyer sur Entrée pour cliquer :)")
credits_ects = 0
while True:
    input()
    credits_ects+=1
    print(f"Vous avez {credits_ects} crédits ECTS!")
    if (math.log10(credits_ects)%1==0):
      print(f"Achievement unlocked : Obtenir {credits_ects} crédits !")
