from math import pi

a, n = map(float, input().split())

rad = n / (2*pi)
area = pi * (rad**2)

if area >= a:
	print('Diablo is happy!')
else:
	print('Need more materials!')
