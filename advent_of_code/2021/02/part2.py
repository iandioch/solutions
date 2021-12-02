import sys
x = 0
y = 0
aim = 0
for line in sys.stdin.readlines():
    command, dist = line.split()
    dist = int(dist)
    if command == 'forward':
        x += dist
        y += aim*dist
    elif command == 'up':
        aim -= dist
    else: # 'down'
        aim += dist

print(x*y)
