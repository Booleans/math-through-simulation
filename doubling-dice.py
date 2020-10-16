'''
From Reddit:

I have a question about calculating expected value for something. Lets say I have a set of six sided dice. 
The sides of each die are as follows: (0, 0, 1, 1, 2, and x2). 
If you roll a x2 on one die it doubles the value of all the other dice. 
If you roll multiple x2 they stack (x4, x8, etc). 
How would you calculate the expected value for rolling a finite number of these dice?
'''

import numpy as np

n_dice = 6
n_sims = 10**7
SIDES = np.array([0, 0, 1, 1, 2, 3])
# A 3 represent a x2 die.
rolls = np.random.choice(SIDES, size=(n_sims, n_dice), replace=True)
number_of_doubles = np.sum(rolls == 3, axis=1)
# Replace all 3 values with 0 to not affect the sums.
sums_non_doubling_dice = np.sum(np.where(rolls != 3, rolls, 0), axis=1)
totals = sums_non_doubling_dice * 2**number_of_doubles

np.mean(totals)
