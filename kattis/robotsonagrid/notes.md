Walking only right and down, the number of ways to get to square (X,Y) is the sum of the number of ways to get to square (X,Y-1) and to square (X-1,Y). You can pre-fill the leftmost column and topmost row before iterating, to make this easier.

If square(N-1,N-1) is not reachable in this way, just do a floodfill from square (0,0) and see if (N-1,N-1) is ever visited.

Don't forget to give answers `% (2^32 - 1)`.

This was the first python solution submitted. Python3 times out, Python2 runs in 0.95s.
