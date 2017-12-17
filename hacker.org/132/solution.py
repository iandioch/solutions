import sys

a = sys.stdin.readlines()
b = ''

for i in range(192):
	s = a[i].strip()
	d = len(a[i]) - len(s)
	if d % 2 == 0:
		b += '0'
	else:
		b += '1'

for i in range(len(b)//8):
	s = b[i*8:(i+1)*8]
	n = int(s, 2)
	print(chr(n), end='')
