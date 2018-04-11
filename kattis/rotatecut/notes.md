Perform the given simulation, flipping and cutting the string, with the following additions:

- If the change would do nothing (ie. `len(s)//4 == 0`), then quit, as no more changes can be made (and the input N is up to 10^9, so you need this speedup).
- Keep track of the orientation of the string as you flip, as at the end if it is upside-down (ie. an odd number of flips), you'll need to re-flip it the right way up.
