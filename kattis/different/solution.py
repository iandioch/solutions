s = raw_input()
while s is not None:
	parts = s.split()
	a = int(parts[0])
	b = int(parts[1])
	print abs(a-b)
	try:
		s = raw_input()
	except:
		break
