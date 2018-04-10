First, fill a matrix with the distance from every point to the nearest tree. I used a queue for this, starting at the position of each tree and building up the distances.

Then, using a priority queue sorted by the minimum distance to any tree so far in decreasing order, starting at the given starting position, find the first path you can to the given goal. I used python's heapq module for this, and used the negative of the distance to the nearest tree, to sort it correctly.

This runs in 0.93s in Python2.
