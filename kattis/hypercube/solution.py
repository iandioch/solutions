def binsearch(query, lo, hi, index, reverse=False):
	if index == len(query):
		return lo
	if lo == hi:
		return lo
	b = query[index]
	in_first_half = True
	if b == '0' and reverse:
		in_first_half = False
	if b == '1' and not reverse:
		in_first_half = False
	if in_first_half:
		return binsearch(query, lo+(hi-lo)/2, hi, index+1, False)
	else:
		return binsearch(query, lo, hi-(hi-lo)/2, index+1, True)

n, a, b = raw_input().split()
n = int(n)

m = 2**n
i = binsearch(a, 0, m, 0, False)
j = binsearch(b, 0, m, 0, False)

print i-j-1
