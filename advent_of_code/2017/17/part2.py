from collections import defaultdict


step = int(input())
curr = 0
after = None
for buffer_length in range(1, 50000000 + 1):
	curr = ((curr + step + 1) % buffer_length) 
	if curr == 0:
		# Goes after the zero
		after = buffer_length

print(buffer)
