'''
Bobo the amoeba has a 25%, 25%, and 50% chance of producing 0, 1, or 2 offspring respectively.
Each of Bobo's descendants also have the same probabilities.
What is the probability that Bobo’s lineage dies out?
'''

import random

def get_num_offspring():
    num = random.random()
    if num < .25:
        return 0
    if num < .50:
        return 1
    else:
        return 2

n_sims = 10**4
n_lineage_dead = 0
# How many amoebas should reproduce before we conclude the lineage will live on?
min_amoebas = 500

for _ in range(n_sims):
    n_amoebas_reproduced = 0
    amoebas = [1]
    while amoebas and n_amoebas_reproduced < min_amoebas:
        amoebas.pop()
        n_amoebas_reproduced += 1
        for _ in range(get_num_offspring()):
            amoebas.append(1)
    if len(amoebas) == 0:
        n_lineage_dead += 1

# Goal is to see percentage of time the lineage died out. Answer approximates 50%.
print(n_lineage_dead/n_sims)
