num_tests = int(input())
for test in range(num_tests):
	n, m, l = map(int, input().split())
	causes_to_fall = {}
	for i in range(m):
		x, y = map(int, input().split())
		if x in causes_to_fall:
			causes_to_fall[x].append(y)
		else:
			causes_to_fall[x] = [y]
	fallen = set()
	q = []
	qi = 0
	for i in range(l):
		q.append(int(input()))

	while qi < len(q):
		d = q[qi]
		qi += 1
		if d in fallen:
			continue
		fallen.add(d)
		if d in causes_to_fall:
			for e in causes_to_fall[d]:
				q.append(e)
		
	print(len(fallen))
	
