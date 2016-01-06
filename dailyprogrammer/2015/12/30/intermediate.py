import sys

# get number of ways in width*height grid moving horizontally, vertically and diagonally
def countWays(width, height):
	if width == 0 or height == 0:
		return 1
	numWays = [[0 for y in range(height)] for x in range(width)]

	for x in range(width):
		numWays[x][0] = 1

	for y in range(height):
		numWays[0][y] = 1

	for x in range(1, width):
		for y in range(1, height):
			numWays[x][y] = numWays[x-1][y-1] + numWays[x][y-1] + numWays[x-1][y]
	return numWays[width-1][height-1]

# get all the positions of the Xs in the grid
def getXs(grid):
	w = len(grid)
	h = len(grid[0])

	xs = []
	for x in range(w):
		for y in range(h):
			if grid[x][y] == 'X':
				xs.append((x, y))

	return xs

# given the grid, get the number of ways through, or return an error
def compute(grid):
	sortedXs = sorted((x, len(grid[0])-y) for x,y in getXs(grid)) # sort the grid positions by the X then the Y
	ans = 1
	for i in range(len(sortedXs)-1):
		if sortedXs[i][1] > sortedXs[i+1][1]:
			return -1

		w = abs(sortedXs[i+1][0] - sortedXs[i][0]) + 1
		h = abs(sortedXs[i][1] - sortedXs[i+1][1]) + 1
		ans *= countWays(w, h)
	return ans

def main():
	parts = sys.stdin.readline().split(",")
	width = int(parts[0])
	height = int(parts[1])
	grid = [['.' for y in range(height)] for x in range(width)]
	for y in range(height):
		line = sys.stdin.readline().strip()
		for x in range(len(line)):
			grid[x][y] = line[x]

	ans = compute(grid)
	if ans <= 0:
		print "ERROR: Invalid grid."
	else:
		print ans

if __name__ == '__main__':
	main()