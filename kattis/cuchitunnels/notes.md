This is a graph construction problem.

Place node 1. This will always be the head of the tree, with no parent.

Any new node will always either connect to the previous highest node, or some parent up the tree of that node. This will always be true, as if there was some lower-numbered node `X` wanted a new connection, the subsequent node `X+1` should have connected to it, and any other nodes `X+N` since should either have connected to a descendant of `X`, or to `X` itself, so `X` will always be in the tree of possible connections for a new node `Y` when following the above method.

This solution runs in 0.02s in python 3, or 0.04s in python 2.
