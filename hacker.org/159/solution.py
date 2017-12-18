s = input()
t = []
for i in range(len(s)//2):
	n = int(s[i*2:i*2+2], 16)
	t.append(n)

for k in range(256):
	for x in range(256):
		o = []
		b = k
		for e in t:
			o.append(e^b)
			b = (b + x) % 256
		f = ''.join(map(chr, o))
		if 'th' in f:
			try:
				print(f)
			except Exception as e:
				pass
