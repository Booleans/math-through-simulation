```
A city with 6 districts has 6 robberies in a particular week. Assume the robberies are
located randomly, with all possibilities for which robbery occurred where equally likely.
What is the probability that some district had more than 1 robbery?

Solving by-hand yields 1 - 6!/6^6 = .98456.
```

import numpy as np

n_sims = 10**7

DISTRICTS = np.arange(6)
robberies = np.random.choice(DISTRICTS, size=(n_sims,6), replace=True)
sorted_robberies = np.sort(robberies)
# After sorting the districts that were robbed, you can take the difference between sequential district numbers with np.diff.
# If all differences are greeater than 0 then no district was robbed more than once.
1 - np.mean(np.all(np.diff(sorted_robberies), axis=1)) # 0.98455182