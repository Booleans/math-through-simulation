# Math Through Simulation

![Vampires](https://github.com/Booleans/math-through-simulation/blob/master/img/WWDitS.png)

Thanks to the power of modern computers and the law of large numbers, certain math problems can be solved through simulation. Take this data science interview question as an example:

*Every night between 7 PM and midnight, two computing jobs from two different sources are randomly started with each one lasting an hour.
Unfortunately, when the jobs simultaneously run, they cause a failure in some of your company's other nightly jobs, resulting in downtime that costs $1,000. The CEO needs you to tell her the annual cost of this issue.* 


With the help of (Python) code you can simply simulate these nightly jobs tens of millions of times and see how often they tend to overlap.

```Python
import numpy as np

# Simulate the second that each process starts on. We could be more precise if we went down to smaller increments of time.
process_1 = np.random.randint(0, 5*60*60, size=10**7)
process_2 = np.random.randint(0, 5*60*60, size=10**7)
# Each job is an hour long so there's an overlap if their starting times are within 3,600 seconds of each other.
overlap_percentage = np.mean(np.abs(process_1 - process_2) <= 3_600)
annual_cost = overlap_percentage * 365 * 1000
```

#### For My Students:

Please first attempt to find the closed-form solution with pen and paper. Afterwards, confirm your solution through simulation. I would prefer you use vectorized NumPy operations for speed and efficiency. However, if you are still uncomfortable "thinking in NumPy" then you are welcome to use pure Python and we can discuss how your code might be modified. 

![NumPy Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/NumPy_logo.svg/2000px-NumPy_logo.svg.png)
