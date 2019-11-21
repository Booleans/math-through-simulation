'''
Consider a well-suffled deck of cards labeled 1 through n. You flip over the cards one-by-one, saying the numbers
1 through n as you do so. You win the game if, at some point, the number you say aloud if the number of the card
being flipped over. What is the probability of winning?

This should work out to approximately 1-(1/e) = .632. Let's use a deck of 100 cards in the simulation.
'''
import numpy as np

n_trials = 10**5

cards = np.array(range(100))
indices = np.array(range(100))
# Trials is a matrix with dimensions (n_trials, 100) where each row is the shuffled numbers 0 through 99.
trials = np.concatenate([np.random.choice(cards, size=100, replace=False).reshape(1, 100) for _ in range(n_trials)], axis=0)
# A match is where the card number is equal to its index position.
matches = np.any(trials == indices, axis=1)

p_winning = np.sum(matches)/n_trials
p_winning # ~0.63116