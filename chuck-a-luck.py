'''
Problem #6 in "Fifty Challenging Problems in Probability" by Frederick Mosteller.

Chuck-a-Luck 

Chuck-a-Luck is a gambling game often played at carnivals and gambling houses. A player may bet on any of the numbers
1, 2, 3, 4, 5, or 6. Three dice are rolled. If a player's number appears on one, two, or three of the dice, he receives
respectively one, two, or three times his original stake plus his own money back; otherwise he loses his stake. What is the
player's expected loss per unit stake? (Actually the player may distribute stakes on several numbers, but each such stake can
be regarded as a separate bet.)
'''

import numpy as np

n_sims = 10**7
# We can simulate the number of matching fair dice by drawing samples from a binomial distribution with n=3, p=1/6.
num_matching_rolls = np.random.binomial(n=3, p=1/6, size=n_sims)
# If none of the dice were matching then we've lost our entire stake, represented here by turning zeros into -1.
stakes_won = np.where(num_matching_rolls == 0, -1, num_matching_rolls)

print(np.mean(stakes_won))
# My result was -0.0780561, matching my closed-form solution of -17/216.