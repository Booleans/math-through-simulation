'''
https://en.wikipedia.org/wiki/Birthday_problem

In a set of n randomly chosen people, there is a probability that at least one pair of people will share a birthday.
At what value of n does that probability exceed 50%?
'''

import numpy as np
import pandas as pd

def birthday_problem_simulation(n_people, n_simulations):
    # Assuming a uniform distribution of birthdays and ignoring leap years.
    random_birthdays = np.random.randint(365, size=n_people*n_simulations)
    # Create a matrix where each row represents a simulation of n_people's birthdays.
    reshaped_birthdays = random_birthdays.reshape(n_simulations, n_people)
    # Converting to a dataframe allows us to use the nunique function along each row.
    df = pd.DataFrame(reshaped_birthdays)
    # If the number of unique birthdays in a row is less than the number of people in a row then there's been a matching birthday.
    n_matches = np.sum(df.nunique(axis=1) < n_people)
    p_match = n_matches/n_simulations
    return p_match

for n in range(2, 366):
    if birthday_problem_simulation(n_people=n, n_simulations=10**5) > .50:
        print(n) # We exceed 50% starting at 23 people in a group.
        break
