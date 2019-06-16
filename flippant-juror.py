'''
Problem #3 in "Fifty Challenging Problems in Probability" by Frederick Mosteller.

The Flippant Juror

A three-man jury has two members each of whom independently has a probability p of making the correct decision and
a third member who flips a coin for each decision (majority rules). A one-man jury has probability p of making the 
correct decision. Which jury has the better probability of making the correct decision?

Solving by hand yields an equal probability for both juries. Let's confirm programmatically. 
'''

import random

n_sims = 10**7
p = .80
n_success_1_person_jury = 0
n_success_3_person_jury = 0

for _ in range(n_sims):
    # Do 3 person jury first.
    correct_jurors = 0
    # Evaluate juror 1.
    if random.random() <= p:
        correct_jurors += 1
    # Evaluate juror 2.
    if random.random() <= p:
        correct_jurors += 1
    # Evaluate juror 3, the coin flipper.
    if random.random() <= .5:
        correct_jurors += 1
            
    if correct_jurors >= 2:
        n_success_3_person_jury += 1
    
    # Look at the 1 person jury.
    if random.random() <= p:
        n_success_1_person_jury += 1
        
        
print(n_success_3_person_jury/n_success_1_person_jury) 
# 1.0003677286257737, they are equally probable. 