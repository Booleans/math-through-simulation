'''
You're given a fair coin. You keep flipping the coin, keeping tracking of the last three flips.
For example, if your first three flips are T-H-T, and then you flip an H, your last three flips are now H-T-H. 

You keep flipping the coin until the sequence Heads Heads Tails (HHT) or Heads Tails Tails (HTT) appears. 
Is one more likely to appear first? If so, which one and with what probability?
'''
import random

simulations = 10**5

SIDES = ('H', 'T')
wins = 0

for _ in range(simulations):
    last_3 = [random.choice(SIDES) for _ in range(3)]

    while last_3 not in (['H', 'H', 'T'], ['H', 'T', 'T']):
        new_flip = random.choice(SIDES)
        last_3[0], last_3[1], last_3[2] = last_3[1], last_3[2], new_flip

    if last_3 == ['H', 'H', 'T']:
        wins += 1

win_proportion = wins/simulations
print(win_proportion)
