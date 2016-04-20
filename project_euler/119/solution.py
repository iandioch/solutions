powers = []

for i in xrange(2, 100):
	for j in xrange(1, 30):
		powers.append(i**j)

powers = sorted(powers)

def valid(n):

	s = str(n)
	q = 0
	for c in s:
		q += int(c)
	if q == 1:
		return False
	p = 1
	while q**p < n:
		p += 1
	return q**p == n

c = 0

a = set()
for i in powers:
	if i < 10:
		continue
	if i in a:
		continue
	if valid(i):
		c += 1
		a.add(i)
		print c, i
		if c >= 30:
			break
