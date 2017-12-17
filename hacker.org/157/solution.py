s = input()
for i in range(len(s)//2):
	t = s[i*2:i*2 + 2]
	n = int(t, 16)
	print(chr(n^79), end='')
print()
