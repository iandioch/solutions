a = raw_input()
b = raw_input()
if len(a) < len(b):
	a = '0' * (len(b)-len(a)) + a
else:
	b = '0' * (len(a)-len(b)) + b


#c = a[:len(a)-len(b)]
#d = b[:len(b)-len(a)]
c, d = '', ''
for i in xrange(len(a)):
	if i >= len(b):
		break
	if a[i] < b[i]:
		d += b[i]
	elif a[i] > b[i]:
		c += a[i]
	else:
		c += a[i]
		d += b[i]

print int(c) if len(c) else 'YODA'
print int(d) if len(d) else 'YODA'

