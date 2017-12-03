def calc(n):
	highest_square = 1
	while (highest_square+2)**2 < n:
		highest_square += 2
	side = highest_square+2
	progress = n - (highest_square**2)
	dist_from_corner = (progress) % (side-1)

	dist_from_centre = abs(dist_from_corner - (side//2))
	radius = side//2
	return dist_from_centre + radius

n = int(input())
print(calc(n))
