parts = [int(x) for x in raw_input().split()]
b = parts[:6]
s1 = parts[6]
s2 = parts[7]

b = sorted(b, reverse=True)
first = None
second = None
found = False

for i in xrange(1, 6):
	for j in xrange(i+1, 6):
		t = b[0] + b[i] + b[j]
		if t == s1:
			first = [str(b[0]), str(b[i]), str(b[j])]
			second = [str(k) for k in b if (str(k) not in first)]
			found = True
			break
		if t == s2:
			second = [str(b[0]), str(b[i]), str(b[j])]
			first = [str(k) for k in b if (str(k) not in second)]
			found = True
			break
	if found:
		break

print ' '.join([' '.join(first), ' '.join(second)])

