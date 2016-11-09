#!/usr/bin/python2
# inspired by some python at https://pythontips.com/2013/09/01/sudoku-solver-in-python/
# however it runs much too slowly with all the list concats, etc.
import collections 

def same_row(x, y):
	return (x//9 == y//9)

def same_column(x, y):
	return (x-y) % 9 == 0

def same_square(x, y):
	return (x//27 == y//27 and (x%9)//3 == (y%9)//3)

def solve(g):
	count = 0
	q = collections.deque()
	q.append(g)
	while True:
		count += 1
		a = q.popleft()
		i = a.find('0')
		if i == -1:
			return a, count

		taken = set()
		for j in xrange(len(a)):
			if same_row(i, j) or same_column(i, j) or same_square(i, j):
				taken.add(a[j])

		for n in '123456789':
			if n not in taken:
				q.append(a[:i] + n + a[i+1:])

total = 0
for i in xrange(50):
	s = raw_input()
	a = ''.join([raw_input() for x in xrange(9)])
	ans, cost = solve(a)
	print "%s: ans = %s, iters = %s" % (s, ans, cost)
	total += int(ans[0:3])
print total
