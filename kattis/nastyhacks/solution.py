n = int(input())
for _ in range(n):
	a, b, c = map(int, input().split())
	p = b - c
	if a == p:
		print('does not matter')
	elif a > p:
		print('do not advertise')
	else:
		print('advertise')
