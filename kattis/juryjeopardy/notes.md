Perform the simulation as given, walking the character through the maze. Keep all points visited in a set. After the route has finished, the height of the maze is `(maxy - miny + 1)`, with an extra `+ 2` for the top and bottom walls. The width is `(maxx - minx + 1)` with an extra `+ 1` for the right wall (as the left wall will already be in the path).

Now just output `#` for everywhere not in the path, or `.` for everywhere in the path.
