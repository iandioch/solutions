An all-pairs shortest-paths is best solved by Floyd-Warshall. However, this one also includes negative edges. In this case, complete a normal Floyd-Warshall, and then afterwards try to find negative loops. Any node with a negative loop from itself to itself, will mark all nodes with edges from it as infinitely looping too.

Too slow for python3, but in python2 it runs in 0.93s.
