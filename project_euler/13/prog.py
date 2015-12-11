sum = 0

with open("nums.txt", 'r') as file:
	lines = file.readlines()
	for line in lines:
		num = int(line)
		sum += num

print sum
