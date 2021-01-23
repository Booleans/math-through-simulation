'''
Let's say you are playing a coin flip game. You start with $30. If you flip heads, you win $1, but if you get tails, you lose $1. 
You keep playing until you run out of money (have $0) or until you win $100. 

What is the probability that you win $100?

This is a data scientist interview question that was asked by Robinhood.
'''

import random

# You may want to run fewer than 1 million simulations for the sake of time.
trials = 10**6
successes = 0

for _ in range(trials):
    money = 30
    while money not in (0, 100):
           money += random.choice([-1, 1])
    if money == 100:
        successes += 1

print(successes/trials) # ~.30 = 30%