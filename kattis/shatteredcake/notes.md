A simple ad-hoc maths problem. Just get the total area of all pieces and divide by the given width.

However, the input is large, my first solution timed out in Python3. You need to use `stdin.readline()` and not `input()` in order to get in under the time limit. Python2 is still much faster. I also wrote a C solution before I figured out how to read input faster in Python. I then sped up the python a little bit by keeping a pointer to `stdin.readline`, so that it didn't have to search the global scope every time it was called.

Runs in:

- 0.42s in C
- 0.72s in Python2
- 4.3s in Python3 
