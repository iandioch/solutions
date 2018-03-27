Given inputs A, B, C, D, E (these are: total games, games won, games drew, games lost, points).

We know: 

A = B + C + D
E = 3B + C

We also know there is only one valid arrangement of values for each input.

If there is only one possible arrangement, we must know either A or D (otherwise we could keep incrementing them and have multiple possible arrangements). The only case where this isn't true is if A == 100 and D = 0.

Now, given B and C, we can derive A, D, and E.

This means we can iterate over B and C and find a valid arrangement. If we are given either B or C, we can just limit our search.

Runs in 0.01s.
