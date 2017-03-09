n_tests = int(input())
for test in range(n_tests):
	n = int(input())
	d = set()
	for _ in range(n):
		d.add(input())
	print(len(d))
