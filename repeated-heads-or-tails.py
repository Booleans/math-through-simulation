'''
All of Statistics, Chapter 01 Problem 13

Suppose that a fair coin is tossed repeatedly until both a head and a tail have appeared at least once. 
What is the probability that 3 throws will be required?
'''

import numpy as np

trials = 10**7
# Use 0/1 for the sides of the coin instead of T/H.
flips = np.random.randint(2, size=(trials, 3))
diffs = np.diff(flips)
np.mean((diffs[:, 0] == 0) & (diffs[:, 1] != 0)) # 1/4
