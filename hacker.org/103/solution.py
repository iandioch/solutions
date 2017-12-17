# According to http://www.pictaculous.com, the image colour is #9C54C6
# Other sites gave different values, apparently they're wrong
s = '9C54C6'
a = ''
for i in range(3):
	f = s[i*2:i*2+2]
	n = int(s[i*2:i*2 + 2], 16)
	t = bin(n)[2:].zfill(8)
	a += t
print(int(a, 2))
