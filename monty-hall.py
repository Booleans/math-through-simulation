import numpy as np

def monty_hall(switch=True, n_games=10**7):
    door_choices = np.random.randint(0, 3, size=n_games)
    door_correct = np.random.randint(0, 3, size=n_games)

    if switch == True:
        return np.sum(door_choices != door_correct)/n_games
    else: 
        return np.sum(door_choices == door_correct)/n_games

print(monty_hall(switch=True)) # ~.666
print(monty_hall(switch=False)) # ~.333