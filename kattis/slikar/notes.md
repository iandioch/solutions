Given the map, we can compute how long it will take for the flood to reach each square using a flood fill / BFS / DFS / whatever. I used a priority queue here.

I then did exactly the same computation to figure out how long it would take to walk from square S to square D, with the added limit of not walking into a square if the flood would reach it first (by looking up the previously computed table).

Just output the best time to D (or KAKTUS if there was no path).

Runs in 0.04s in Python 3. Could speed it up by eg. Not putting out-of-bounds squares into the priority queues, but that's not necessary.
