import sys
d = {}

s = raw_input()
while s != '':
	t = s.split()
	d[t[1]] = t[0]
	s = raw_input()

lines = sys.stdin.readlines()
for line in lines:
	if line[:-1] in d:
		print d[line[:-1]]
	else:
		print 'eh'
