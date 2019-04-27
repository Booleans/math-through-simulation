# Robert asked me how to simulate to approximate the probability of drawing socks from his daughter's sock drawer.
# His daughter has 8 pairs of socks and he drew 5 unique individual socks, following by 2 individual socks that matched.

import numpy as np

socks = list(range(8)) * 2
n_sims = 10**6
n_success = 0

for _ in range(n_sims):
    sample = np.random.choice(socks, size=7, replace=False)
    if (sample[-1] == sample[-2]) and (len(np.unique(sample)) == 6):
        n_success += 1
        
n_success/n_sims
# ~0.022494