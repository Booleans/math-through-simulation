'''
Bobo the amoeba has a 25%, 25%, and 50% chance of producing 0, 1, or 2 offspring respectively.
Each of Bobo's descendants also have the same probabilities.
What is the probability that Bobo’s lineage dies out?
'''

import random

OFFSPRING = (0, 1, 2, 2)

n_sims = 10**6
n_lineage_dead = 0
# How many amoebas should reproduce before we conclude the lineage will live on?
min_amoebas = 20

for _ in range(n_sims):
    amoebas = [1]
    while amoebas and len(amoebas) < min_amoebas:
        amoebas.pop()
        for _ in range(random.choice(OFFSPRING)):
            amoebas.append(1)
    if len(amoebas) == 0:
        n_lineage_dead += 1
        
# Goal is to see percentage of time the lineage died out. Answer approximates 50%.
print(n_lineage_dead/n_sims)
