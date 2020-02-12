milestones = dict()  # maps milestone numbers to achievement names
milestones[1] = "Rambo: First Credit"
milestones[6] = "C'est ça une UV ?"
milestones[20] = "Sur un malentendu..."
milestones[60] = "...ça peut passer"
milestones[96] = "Seuil de crédits scientifiques atteint... LIKE A BOSS"
milestones[180] = "Enfin diplômé"

achievement_list = dict()
achievement_list["Morse"] = False
for nb in milestones:  # Adding milestones achievements to achievement list
    achievement_list[milestones[nb]] = False


# If the input achievement exists and is unearned, earns the achievement
def earn(achievement_name):
    if achievement_name in achievement_list and not achievement_list[achievement_name]:
        print(f"Achievement unlocked : {achievement_name}")
        achievement_list[achievement_name] = True
