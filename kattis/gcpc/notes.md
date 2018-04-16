Can keep a set `better` of all teams ahead of team 1 in the standings. If team 1 solves a new problem, remove all members of `better` that are now worse than team 1. If another team solves a new problem, see if it is now ahead of team 1, and add it to the set.

The position of team 1 is always `len(better) + 1`.
