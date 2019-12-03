'''
You are trapped in a dark cave with three indistinguishable exits on the walls. One exit takes you 3 hours to travel and 
takes you outside. One of the other exits takes 1 hour to travel and the other takes 2 hours, but both drop you back
in the original cave through the ceiling, which is unreachable from the floor of the cave. You have no way of marking which
exits you've attempted. What is the expected time it takes for you to get outside?
'''

import random

ROUTES = tuple('ABC')
route_times = {'A':3, 'B':1, 'C':2}
n_sims = 10**6
total_time = 0

for _ in range(n_sims):
    while True:
        path = random.choice(ROUTES)
        total_time += route_times[path]
        if path == 'A':
            break
            
print(total_time/n_sims) # Yields 6.001775 hours, confirming my solution of 6 hours.