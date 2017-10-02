MAX = 10001
is_prime = [True]*MAX
primes = set()
for i in range(2, MAX):
	if not is_prime[i]:
		continue
	primes.add(i)
	for j in range(i+i, MAX, i):
		is_prime[j] = False

n = int(input())
for _ in range(n):
	a, b = map(int, input().split())
	if b not in primes:
		print(a, b, 'NO')	
		continue
	seen = set()
	seen.add(b)
	c = b
	valid = True
	while c != 1:
		c = sum([int(d)**2 for d in str(c)])
		if c in seen:
			valid = False
			break
		seen.add(c)
	if valid:
		print(a, b, 'YES')
	else:
		print(a, b, 'NO')
		
