'''
Four Person Elevator

There are four people on the ground floor of a building that has five levels not including the ground floor. 
They all get into the same elevator. If each person is equally likely to get on any floor and they leave independently 
of each other, what is the probability that no two passengers will get off at the same floor?

Solving by-hands yields (5*4*3*2)/(5^4) = .192. Let's simulate.
'''

import numpy as np

n_sims = 10**6
sims = np.random.randint(5, size=(n_sims, 4))
n_unique_floors = np.apply_along_axis(lambda x: np.unique(x).size, axis=1, arr=sims)
np.mean(n_unique_floors == 4) # ~0.19195

# Alternative solution without numpy appears faster.

import random

n_sims = 10**6
all_unique = 0

for _ in range(n_sims):
    distinct_floors = {random.randint(1, 5) for _ in range(4)}
    if len(distinct_floors) == 4:
        all_unique += 1
        
all_unique/n_sims
