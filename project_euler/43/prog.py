def has_property(num_str):
	return (int(num_str[1:4]) % 2 == 0) and  (int(num_str[2:5]) % 3 == 0) and (int(num_str[3:6]) % 5 == 0) and (int(num_str[4:7]) % 7 == 0) and (int(num_str[5:8]) % 11 == 0) and (int(num_str[6:9]) % 13 == 0) and (int(num_str[7:10]) % 17 == 0)

print has_property("1406357298")

nums = []

for x in xrange(0,10):
	nums.append(str(x))

while len(nums[0]) < 10: #10!
	new_nums = []
	for num in nums:
		for x in xrange(0,10):
			if not str(x) in num:
				new_nums.append(num + str(x))
	nums = new_nums

s = 0

for num in nums:
	if has_property(num):
		s += int(num)

print s
