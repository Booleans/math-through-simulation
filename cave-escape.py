'''
FILL THIS IN
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