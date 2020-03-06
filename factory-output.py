'''
Problem #34 in "Fifty Challenging Problems in Probability" by Frederick Mosteller.

Birthday Holidays

Labor laws in Erewhon require factory owners to give every worker a holiday whenever one of them has a birthday and to hire
without discrimination on the grounds of birthdays. Except for these holidays they work a 365-day year. The owners want to 
maximize the expected total number of man-days worked per year in a factory. How many workers do factories have in Erewhon?
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

# The simulation does not tend to return a consistent answer due to how similar the factory output is for values such as 
# 364, 365, 366, etc. I had to use numpy to get a solution.

n_employees = np.arange(400)
factory_output = 365*n_employees*((364/365)**n_employees)
np.argmax(factory_output) # 365
