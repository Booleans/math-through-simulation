'''
Problem #3 in "Fifty Challenging Problems in Probability" by Frederick Mosteller.

The Flippant Juror

A three-man jury has two members each of whom independently has a probability p
of making the correct decision and a third member who flips a coin for each 
decision (majority rules). A one-man jury has probability p of making the 
correct decision. Which jury has the better probability of making the correct 
decision?

Solving by hand yields an equal probability for both juries. Let's test this
 with simulation. 
'''

import numpy as np

# Draw 2 jurors from a binomial distribution with 2 trials and probability p.
# Then draw one juror from a coin flip.
jurors_correct = (np.random.binomial(2, p, size=n_sims) + 
                  np.random.binomial(1, .50, size=n_sims))
percent_correct = np.mean(jurors_correct >= 2)

print(percent_correct) 
# 0.6002154, which is just p, the probability of the one-man jury being correct.