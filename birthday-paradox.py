'''
https://en.wikipedia.org/wiki/Birthday_problem

In a set of n randomly chosen people, there is a probability that at least one pair of people will share a birthday.
At what value of n does that probability exceed 50%?
'''

import numpy as np

def birthday_problem_simulation(n_people, n_sims=10**5):
    # Assuming a uniform distribution of birthdays and ignoring leap years.
    birthdays = np.random.randint(365, size=(n_people, n_sims))
    num_unique_birthdays = np.apply_along_axis(lambda x: np.unique(x).size, axis=0, arr=birthdays)
    # If the number of unique birthdays in a row is less than the number of people in a row then there's been a matching birthday.
    overlaps = num_unique_birthdays < n_people
    return np.mean(overlaps)

for n in range(2, 366):
    if birthday_problem_simulation(n_people=n, n_sims=10**5) > .50:
        print(n) # We exceed 50% starting at 23 people in a group.
        break
