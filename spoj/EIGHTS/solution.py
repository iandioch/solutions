def quick_find(k):
	d = [192, 442, 692, 942]
	t = int((k-1)/4)
	j =(k-1)  % 4
	return int(t*1000 + d[j])

n = int(input())
for i in range(n):
	k = int(input())
	print(quick_find(k))
