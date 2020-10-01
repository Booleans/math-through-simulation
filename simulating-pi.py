# Imagine a 2x2 square, with a unit circle in the center.
# So both our x and y coordinates can range from -1 to 1.

import numpy as np

n_sims = 10**8
# Generate x and y coordinates of points falling randomly on the 2x2 square.
coords = np.random.uniform(-1, 1, size=(n_sims, 2))
# A point falls within the unit circle if x**2 + y**2 <= 1
in_circle = np.sum(coords**2, axis=1) <= 1
proportion_in_circle =  np.mean(in_circle)
# The proportion of the random points that fall within the circle can be used to estimate π. 
pi_hat = 4*proportion_in_circle
