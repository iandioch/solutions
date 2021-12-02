import sys
x = 0
y = 0
for line in sys.stdin.readlines():
    command, dist = line.split()
    dist = int(dist)
    if command == 'forward':
        x += dist
    elif command == 'up':
        y -= dist
    else:
        y += dist

print(x*y)
