for s in input().strip().split('%'):
	if len(s) == 0:
		continue
	print(chr(int(s, 16)), end='')
print()
