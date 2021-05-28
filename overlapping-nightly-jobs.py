# Every night between 7 PM and midnight, two computing jobs from two different sources are randomly started with each one lasting an hour.
# Unfortunately, when the jobs simultaneously run, they cause a failure in some of the other company’s nightly jobs, 
# resulting in downtime for the company that costs $1,000. 

# The CEO needs you to tell her the annual cost of this issue. Write a simulation to approximate the annual cost. 

import numpy as np
# There are five hours in this interval and each job lasts one hour, or 20% of the total interval.
# Let's use np.random.random to generate a number between 0 and 1, representing the position in the interval that the jobs start.
# If the difference between start times is <= 20% of the interval then there's an overlap. 
process_1 = np.random.random(size=10**7)
process_2 = np.random.random(size=10**7)
overlap_percentage = np.mean(np.abs(process_1 - process_2) <= 0.20)
annual_cost = overlap_percentage * 365 * 1000

print(annual_cost)
