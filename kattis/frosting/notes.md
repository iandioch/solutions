An ad-hoc arrays implementation problem. The `O(n^2)` trivial solution is too slow. Instead, you must realise that you can do it in `O(2*n)`, if you sum together all of the grid heights at the beginning in 3 buckets, and cycle them while computing the totals.

Runs in 0.02s in C.
