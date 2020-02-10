milestone_names = dict()
milestone_names[1] = "Rambo: First Credit"
milestone_names[6] = "C'est ça une UV ?"
milestone_names[20] = "Sur un malentendu..."
milestone_names[60] = "...ça peut passer"
milestone_names[96] = "Seuil de crédits scientifiques atteint... LIKE A BOSS"
milestone_names[180] = "Enfin diplômé"

achievement_list = dict()
achievement_list["Morse"] = False
achievement_list[milestone_names[1]] = False
achievement_list[milestone_names[6]] = False
achievement_list[milestone_names[20]] = False
achievement_list[milestone_names[60]] = False
achievement_list[milestone_names[96]] = False
achievement_list[milestone_names[180]] = False

# If the input achievement exists and is unearned, earns the achievement
def earn_unearned_achievement(achievement_name):

    if achievement_name in achievement_list and not achievement_list[achievement_name]:
            print(f"Achievement unlocked : {achievement_name}")
            achievement_list[achievement_name] = True