A number theory problem, mostly. The implementation counts for a lot here.

We can start counting an integer `d` at 1, and keep adding 1 to the end, until we find a `d` that divides evenly by the inputted number `p`. However, we will start needing bignums, and this will become too slow.

However, the maths still works out ok if we use `d % p` instead of `d`, as the division remainders will be the same, so we will still know when we reach an evenly divisible `d`. This keeps `d` below bignum territory.

We need to consider the case where `p = 1` (which I solve by using `d = (1%p)` as a start, instead of `d = 1`). Then we're done.

Will not run below time in python 3 (because it is all big-nums), but runs in 0.22s in Python2 (the fastest submission in py2 so far on kattis).
