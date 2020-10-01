'''
Problem #2 in "Fifty Challenging Problems in Probability" by Frederick Mosteller.

Successive Wins

To encourage Elmer's promising tennis career, his father offers him a prize if 
he wins at least (at least) two tennis sets in a row in a three-set series to be 
played with his father (F) and the club champion (C) alternatively: 
father-champion-father, or champion-father-champion, according to Elmer's choice.
The champion is a better player than Elmer's father. Which series should Elmer 
choose?

I've worked this out by hand but let's simulate to confirm that C-F-C really is 
the superior strategy.
'''

import numpy as np

p_father = .40
p_champ  = .30
n_sims = 10**7

p_FCF = (p_father, p_champ, p_father)
p_CFC = (p_champ, p_father, p_champ)

games = np.random.binomial(n=1, p=p_FCF, size=(n_sims, 3))
# Elmer wins by winning the middle game and at least 2 total games.
wins = (games[:, 1] == 1) & (np.sum(games, axis=1) >= 2)
win_pct_fcf = np.mean(wins)

games = np.random.binomial(n=1, p=p_CFC, size=(n_sims, 3))
wins = (games[:, 1] == 1) & (np.sum(games, axis=1) >= 2)
win_pct_cfc = np.mean(wins)

print(win_pct_cfc/win_pct_fcf)
# Yields ~1.063, meaning a higher proportion of C-F-C games were won.
