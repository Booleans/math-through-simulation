'''
FILL THIS IN
'''

import numpy as np
import pandas as pd

n_sims = 10**6
n_employees = 350
old_output = 0

while True:
    df = pd.DataFrame(np.random.randint(365, size=n_sims*n_employees).reshape(n_sims, n_employees))
    working_days = 365 - df.nunique(axis=1)
    output = n_employees*np.mean(working_days)
    print(n_employees, output)
    if old_output > output:
        break
    else:
        old_output = output
        n_employees += 1