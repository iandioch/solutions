from math import cos, sin, hypot, radians, atan2, degrees


num_tests = int(input())
for test in range(num_tests):
	num_commands = int(input())
	commands = [input().split() for i in range(num_commands)]
	a = (0, 0, 0)
	for i, command in enumerate(commands):
		d = int(command[1])
		x, y, r = a
		if command[0] == 'fd' or command[0] == 'bk':
			if command[0] == 'bk':
				d *= -1
			x += d*cos(radians(r))
			y += d*sin(radians(r))
		elif command[0] == 'lt':
			r -= d
		else:
			r += d
		a = (x, y, r)
	print(round(hypot(a[0], a[1])))
	
		
