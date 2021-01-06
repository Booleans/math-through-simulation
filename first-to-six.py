'''
Amy and Brad take turns in rolling a fair six-sided die. 
Whoever rolls a "6" first wins the game. Amy starts by rolling first.

What's the probability that Amy wins? Solving by-hand yields 6/11.
'''

import random

trials = 10**6
amy_wins = 0

for _ in range(trials):
    amy_rolling = True
    while True:
        roll = random.randint(1, 6)
        if roll == 6:
            # If Amy is not rolling when the win occurs then we add, False (0) to amy_wins
            amy_wins += amy_rolling
            break
        amy_rolling = not amy_rolling

print(amy_wins/trials) # ~0.545373, 6/11 = 0.545454
