'''
https://en.wikipedia.org/wiki/Monty_Hall_problem
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
'''
import numpy as np

def monty_hall(switching=True, n_games=10**7):
    # We can use a Bernoulli distribution (Binomial with 1 trial) to generate a 1 or 0 that represents
    # whether or not the prize door was selected as the first guess.
    prize_door_selected = np.random.binomial(1, 1/3, size=n_games)

    if switching:
        # When switching you win if the prize door was not your first selection.
        return np.mean(np.logical_not(prize_door_selected))
    else: 
        return np.mean(prize_door_selected)

print(monty_hall(switching=True)) # ~.666
print(monty_hall(switching=False)) # ~.333
