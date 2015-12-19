total = 0

with open("nums.txt", 'r') as file:
	lines = file.readlines()
	for line in lines:
		num = int(line)
		total += num

print str(total)[0:10]
