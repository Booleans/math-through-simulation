'''
https://en.wikipedia.org/wiki/Monty_Hall_problem
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
'''
import numpy as np

def monty_hall(switching=True, n_games=10**7):
    door_choices = np.random.randint(0, 3, size=n_games)
    door_correct = np.random.randint(0, 3, size=n_games)

    if switching:
        return np.sum(door_choices != door_correct)/n_games
    else: 
        return np.sum(door_choices == door_correct)/n_games

print(monty_hall(switching=True)) # ~.666
print(monty_hall(switching=False)) # ~.333
