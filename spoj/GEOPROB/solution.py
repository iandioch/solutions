n = int(input())

for i in range(n):
	b,c,d  = [int(x) for x in input().split(' ')]
	c1 = c-b
	d1 = d-b
	print(c1+c1-d1)
