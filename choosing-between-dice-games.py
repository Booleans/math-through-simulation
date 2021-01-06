'''
This problem was asked by Facebook.

There are two games involving dice that you can play. 
In the first game, you roll two die at once and get the dollar amount equivalent to the product of the rolls. 
In the second game, you roll one die and get the dollar amount equivalent to the square of that value. 
Which has the higher expected value and why?
'''

# We expect game 2 to have the higher expected value. Let's simulate.

import numpy as np

n_sims = 10**7

game_1_rolls = np.random.randint(1, 7, size=(n_sims, 2))
game_1_EV = np.mean(np.product(game_1_rolls, axis=1))

game_2_rolls = np.random.randint(1, 7, size=n_sims)
game_2_EV = np.mean(game_2_rolls**2)

print(game_2_EV > game_1_EV) # True
