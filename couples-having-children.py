'''
You have a group of couples that decides to have children until they've had their first girl. 
Each couple has children until they have their first girl.
How many children is each family expected to have? What is the expected gender ratio?
'''
import random

genders = ('B', 'G')
n_families = 10**6
num_kids = []

for _ in range(n_families):
    kids = []
    while 'G' not in kids:
        kids.append(random.choice(genders))
    num_kids.append(len(kids))
# There will be one girl in each family.
n_girls = n_families
n_boys = sum(num_kids) - n_girls
# Expect 2 children with a gender ratio of 1:1
sum(num_kids)/n_families, n_boys/n_girls
# This is just asking the same binomia distribution problem as the number of fair coin flips required to get one heads flip.