Assign bonds one by one.

If bonds 0..M are assigned to M missions, it does not matter in which order they were assigned when considering where to assign bond M+1. The probability of completing the next mission does not depend on this. This means that we can memoise based on this set of assigned missions (implemented as a bitmask).
