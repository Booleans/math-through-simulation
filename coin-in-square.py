'''
Problem #5 in "Fifty Challenging Problems in Probability" by Frederick Mosteller.

Coin in Square

In a common carnival game a player tosses a penny from a distance of about 5 feet onto the surface of a table ruled in 1-inch 
squares. If the penny (3/4 inch in diameter) falls entirely inside a square, the player receives 5 cents but does not get
his penny back; otherwise he loses his penny. If the penny lands on the table, what are his chances of winning?

Solving by hand yields 1/16, let's simulate to confirm. 
'''

import random

n_sims = 10**7
n_success = 0

for _ in range(n_sims):
    # A coin's center is equally likely to be at any point within a square.
    center_x = random.random()
    center_y = random.random()
    # From the center we can see if any edge exceeds the boundaries of the square. 
    edge_upper = center_y + (3/8)
    edge_lower = center_y - (3/8)
    edge_left = center_x - (3/8)
    edge_right = center_x + (3/8)

    edges = (edge_upper, edge_lower, edge_left, edge_right)
    
    if all(edge > 0 and edge < 1 for edge in edges):
        n_success += 1

print(n_success/n_sims)
# .0625252, ~1/16
