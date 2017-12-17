nums = map(int, input().split(','))

s = ''
for num in nums:
	t = bin(num)[2:].zfill(8)
	s += t

print(int(s, 2))

