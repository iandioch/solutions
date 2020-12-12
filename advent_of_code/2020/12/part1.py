import sys
import math

# pos = tuple(x, y, angle)
def move(pos, opp, dist):
    x, y, angle = pos
    print('In', x, y, angle)
    print('moving', opp, dist)
    if opp == 'n':
        y += dist
    elif opp == 's':
        y -= dist
    elif opp == 'e':
        x += dist
    elif opp == 'w':
        x -= dist
    elif opp == 'l':
        angle += dist
    elif opp == 'r':
        angle -= dist
    elif opp == 'f':
        x += dist*math.cos(math.radians(angle))
        y += dist*math.sin(math.radians(angle))
    print('Out', x, y, angle)
    return (x, y, angle)

pos = (0, 0, 0)
for line in sys.stdin.readlines():
    line = line.strip()
    opp = line[0].lower()
    d = int(line[1:])
    pos = move(pos, opp, d)
print(int(abs(pos[0]) + abs(pos[1])))
