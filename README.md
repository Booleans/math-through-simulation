# Math Through Simulation

![Vampires](https://github.com/Booleans/math-through-simulation/blob/master/img/WWDitS.png)

Thanks to the power of modern computers and the law of large numbers, certain math problems can be solved through simulation. Take this data science interview question as an example:

*Every night between 7 PM and midnight, two computing jobs from two different sources are randomly started with each one lasting an hour.
Unfortunately, when the jobs simultaneously run, they cause a failure in some of your company's other nightly jobs, resulting in downtime that costs $1,000. The CEO needs you to tell her the annual cost of this issue.* 


With the help of (Python) code you can simply simulate these nightly jobs tens of millions of times and see how often they tend to overlap.

```python
import numpy as np
# There are five hours in this interval and each job lasts one hour, or 20% of the total interval.
# Let's use np.random.random to generate a number between 0 and 1, representing the position in the interval that the jobs start.
# If the difference between start times is <= 20% of the interval then there's an overlap. 
process_1 = np.random.random(size=10**7)
process_2 = np.random.random(size=10**7)
overlap_percentage = np.mean(np.abs(process_1 - process_2) <= 0.20)
annual_cost = overlap_percentage * 365 * 1000
```

![NumPy Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/NumPy_logo.svg/2000px-NumPy_logo.svg.png)
