s = input()
t = []
for i in range(len(s)//2):
	n = int(s[i*2:i*2+2], 16)
	t.append(n)

for k in range(0, 257):
	o = ''.join(map(lambda x:chr(x^k), t))
	if 'submit' in o:
		print(o)
