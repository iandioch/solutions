A binary tree problem.

Step the tree recursively. If you've reached the furthest depth, return the value (1 or 0, here represented as binary numbers `10` or `01`) there. If not the furthest depth, then compare the left and right subtrees. If they have the same value (ie. if the bitwise-OR of the tree values is not the binary value `11`, ie. decimal 3), this tree can be merged and just 1 node used. If not, the separate trees must be kept.

Runs in 0.02s in C++.
