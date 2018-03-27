If you look at a brute force solution for N in 1..12, you see a pattern: 

N |f(N)
--|----
1 | 0
2 | 1
3 | 2
4 | 2
5 | 3
6 | 3
7 | 3
8 | 4
9 | 4
10| 4
11| 4
12| 5

ie. In f(N), each number D is repeated D times in the results. This is OEIS sequence A123578 (or A002024 with an inital 0).

We can just build a list with this pattern at init-time, and then query entries in it (or OEIS lists some formulas that are more efficient).

Not sure why this is the pattern though. Requires looking into.
