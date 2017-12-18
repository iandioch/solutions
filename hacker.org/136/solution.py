s = ['0' if c == 'a' else '1' for c in input()]

for i in range(len(s)//8):
	t = ''.join(s[i*8:(i+1)*8])
	n = int(t,2)
	print(chr(n), end='')
