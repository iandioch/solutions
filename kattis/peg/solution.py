import sys

lines = [s[:-1] for s in sys.stdin.readlines()]

ans = 0

for y in range(0, len(lines)-2):
	for x in range(0, len(lines[y])):
		if (lines[y][x] == 'o' and
		    lines[y+1][x] == 'o' and
                    lines[y+2][x] == '.'):
			ans += 1

for y in range(2, len(lines)):
	for x in range(0, len(lines[y])):
		if (lines[y][x] == 'o' and
		    lines[y-1][x] == 'o' and
                    lines[y-2][x] == '.'):
			ans += 1

for y in range(0, len(lines)):
	for x in range(0, len(lines[y])-2):
		if (lines[y][x] == 'o' and
		    lines[y][x+1] == 'o' and
                    lines[y][x+2] == '.'):
			ans += 1

for y in range(0, len(lines)):
	for x in range(2, len(lines[y])):
		if (lines[y][x] == 'o' and
		    lines[y][x-1] == 'o' and
                    lines[y][x-2] == '.'):
			ans += 1

print(ans)
