A DP -ish problem. For point (x, y) in the grid, the quickest time it can be finished is `cost(x, y) + max(time(x-1,y), time(x, y-1)`.

Runs in 0.08s in C++.
