Bellman-Ford is the solution here.

There is a small hiccup in that instead of quitting when you find a negative cycle, you just need to mark all nodes in that as -INFINITY distance. You can just keep looping and checking if any distance is smaller. If no such distance is, you're done. Otherwise, mark it as -INFINITY, and don't check it again.

Solution is too slow in python3, but in python2 it runs in 0.64s.
