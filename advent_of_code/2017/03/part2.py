g = [[1]]

ans = None
upper_right = False
x, y = 1, 0
n = int(input())

def done():
	return x < 0 or y < 0 or x >= len(g[0]) or y >= len(g) or g[y][x] is not None

def get_sum():
	ans = 0
	for i in [x-1, x, x+1]:
		for j in [y-1, y, y+1]:
			if i >= 0 and i < len(g[0]) and j >= 0 and j < len(g):
				# Inside grid.
				if g[j][i] is not None:
					ans += g[j][i]
				
	return ans

def print_grid():
	f = '{:<' + str(len(str(n)) + 1) + '}'
	gap = '_' + ' '*len(str(n))
	for row in g:
		print(('').join(map(lambda v:gap if v is None else f.format(v), row)))
	print('---')


while ans is None:
	print_grid()
	if upper_right:
		done_upper_right = done()
		if done_upper_right:
			h = []
			h = [[None] + row for row in g]
			h.append([None for r in h[-1]])
			g = h
			upper_right = False
			x, y = 0, 0
			continue
		v = get_sum()
		g[y][x] = v
		if v > n:
			ans = v
			break
		if y - 1 < 0:
			x -= 1
		else:
			y -= 1
	else:
		done_lower_left = done()
		if done_lower_left:
			h = [[None for _ in range(len(g[0])+1)]]
			for r in g:
				h.append(r + [None])
			g = h
			upper_right = True
			x, y = len(g[0])-1, len(g)-1
			continue
		v = get_sum()
		g[y][x] = v
		if v > n:
			ans = v
			break
		if y + 1 >= len(g):
			x += 1
		else:
			y += 1

print_grid()
print(v)
