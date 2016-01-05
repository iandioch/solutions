b = 2
m = 10**10
i = 1
while i < 7830457:
	i += 1
	#b = (b * 2) % m
	b = (b << 1) % m

print "exponent:",i
print "result of power of 2:", b

n = (28433 * b + 1)
s = str(n)
print "answer:",s[len(s) - 10:]