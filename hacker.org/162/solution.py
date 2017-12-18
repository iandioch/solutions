s = input()
t = []
for i in range(len(s)//2):
	n = int(s[i*2:i*2+2], 16)
	t.append(n)

for k in range(256):
	o = []
	b = k
	for e in t:
		o.append(e^b)
		b = e
	f = ''.join(map(chr, o))
	try:
		print(''.join(map(chr, o)))
	except Exception as e:
		pass
