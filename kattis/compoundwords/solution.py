import sys
from functools import reduce

words = reduce(list.__add__,
	[line.strip().split() for line in sys.stdin.readlines()])

added = set()
for i, a in enumerate(words):
	for j, b in enumerate(words):
		if i == j:
			continue
		word = a + b
		if word in added:
			continue
		added.add(word)
print('\n'.join(sorted(added)))
		
