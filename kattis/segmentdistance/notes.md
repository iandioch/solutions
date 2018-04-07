[This stackoverflow question](https://stackoverflow.com/questions/2824478/shortest-distance-between-two-line-segments) helped.

1. If the line segments intersect, the answer is 0.
2. Otherwise, the answer is the shortest distance from either point on one line to the other line segment.
    - If the lines are parallel, collinear, then (1) will not work, but (2) will.
