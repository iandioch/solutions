import sys

for line in sys.stdin.readlines():
	for c in line:
		if c in "., !?-0123456789()\"'":
			continue
		if c == c.upper():
			print(c, end='')
