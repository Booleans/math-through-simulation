# Every night between 7pm and midnight, two computing jobs from two different sources are randomly started with each one lasting an hour.
# Unfortunately, when the jobs simultaneously run, they cause a failure in some of the other company’s nightly jobs, resulting in downtime for the company that costs $1,000. 

# The CEO needs you to tell her the annual cost of this issue. 

import numpy as np

# Simulate the second that each process starts on. We could be more precise if we went down to smaller increments of time.
process_1 = np.random.randint(0, 5*60*60, size=10**7)
process_2 = np.random.randint(0, 5*60*60, size=10**7)
# Each job is an hour long so there's an overlap if their starting times are within 3,600 seconds of each other.
overlap_percentage = np.mean(np.abs(process_1 - process_2) <= 3_600)
annual_cost = overlap_percentage * 365 * 1000