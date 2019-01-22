A geometry problem. The points with the largest distances will inevitably be on the convex hull. Thus, run graham scan to get the convex hull, then just use `O(n^2)` iteration to find the largest distance between any two of these points.

Runs in 0.51s in Python3.
