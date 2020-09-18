'''
You're playing casino dice game. You roll a die once. If you reroll, you earn the amount equal to the number on your second roll otherwise, you earn the amount equal to the number on your first roll.

Assuming you adopt a profit-maximizing strategy, what would be the expected amount of money you would win?

This question was asked in a data scientist interview at Tinder.
'''

import numpy as np

for threshold in range(1, 6):
    rolls   = np.random.randint(1, 7, size=10**7)
    rerolls = np.random.randint(1, 7, size=10**7)
    avg_roll = np.mean(np.where(rolls <= threshold, rerolls, rolls))
    print(f'Rerolling all {threshold}s and below yields an average roll of {avg_roll}.')
