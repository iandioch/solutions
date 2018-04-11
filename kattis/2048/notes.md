A painful simulation problem.

I take each direction separately, as I couldn't see a clean way to generalise it.

Whenever two numbers are merged, they cannot be merged again. I put the new number's index in a set, and don't let any merges involve a number in this set. If the number moves into the space of a zero, I remove the old index from the set and add a new one. I continue doing this until no more changes occur.
