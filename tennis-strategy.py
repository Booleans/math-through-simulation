'''
To encourage Elmer's promising tennis career, his father offers him a prize if he wins at least (at least) two tennis
sets in a row in a three-set series to be played with his father and the club champion alternatively:
father-champion-father, or champion-father-champion, according to Elmer's choice. The champion is a better player
than Elmer's father. Which series should Elmer choose?

I've worked this out by hand but let's simulate to confirm that champion-father-champion really is the superior strategy.
'''

import random

p_win = {'F':.40, 'C':.30}
n_wins = {'FCF':0, 'CFC':0}
n_sims = 10**7
player_sequences = ('FCF', 'CFC')

for sequence in player_sequences:
    for _ in range(n_sims):
        previous_win = False
        for player in sequence:
            if random.random() <= p_win[player]:
                if previous_win == True:
                    n_wins[sequence] += 1
                    break
                else:
                    previous_win = True
            else:
                previous_win = False

print(n_wins['CFC']/n_wins['FCF'])
# Yields ~1.0632, meaning more games are won if Elmer chooses the C-F-C sequence of games.