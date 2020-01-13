'''
Problem #19 in "Fifty Challenging Problems in Probability" by Frederick Mosteller.

Isaac Newton Helps Samuel Pepys

Pepys wrote to Newton to ask which of 3 events is more likely: that a person (a) gets at least 1 six when 6 dice are rolled,
(b) at least 2 sixes when 12 dice are rolled, or (c) at least 3 sixes when 18 dice are rolled? What is the answer?

Solving by-hand yields scenario (a) as most likely. 
'''

import numpy as np

for situation_num in range(1, 4):
    n_dice = 6*situation_num
    n_matches = 1*situation_num
    n_trials = 10**6
    
    rolls = np.random.randint(1, 7, size=n_dice*n_trials).reshape(n_trials, n_dice)
    sixes = rolls == 6
    wins = np.sum(sixes, axis=1) >= n_matches
    n_wins = np.sum(wins)
    p_success = n_wins/n_trials
    
    print(f'With {n_dice} dice there is a {p_success} probability of a six being rolled at least {n_matches} times.')

# With 6 dice there is a 0.6649253 probability of a six being rolled at least 1 times.
# With 12 dice there is a 0.618579 probability of a six being rolled at least 2 times.
# With 18 dice there is a 0.5975235 probability of a six being rolled at least 3 times.
