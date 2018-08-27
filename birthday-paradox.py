'''
https://en.wikipedia.org/wiki/Birthday_problem

In a set of n randomly chosen people, there is a probability that at least one pair of people will share a birthday.
At what value of n does that probability exceed 50%?
'''

import numpy as np

def birthday_problem_simulation(n_people, n_simulations):
    # Assuming a uniform distribution of birthdays and ignoring leap years.
    random_birthdays = np.random.randint(365, size=n_people*n_simulations)
    birthday_groups = random_birthdays.reshape(n_simulations, n_people)
    sorted_birthdays = np.sort(birthday_groups)
    diffs = np.diff(sorted_birthdays, axis=1)
    all_unique = np.all(diffs, axis=1)
    # Return the probability of at least 2 people in a group of size 
    # n_people having a matching birthday.
    return 1-(np.sum(all_unique)/n_simulations)	

for n in range(2, 366):
    if birthday_problem_simulation(n_people=n, n_simulations=10**5) > .50:
        print(n) # We exceed 50% starting at 23 people in a group.
        break
