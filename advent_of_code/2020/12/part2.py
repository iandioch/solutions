import sys
import math

# pos = tuple(x, y, angle)
def move(ship, waypoint, opp, dist):
    shipx, shipy = ship
    wayx, wayy = waypoint

    print('Ship pos:', shipx, ', ', shipy)
    print('Waypoint pos:', wayx, ', ', wayy)
    print('moving', opp, dist)
    if opp == 'n':
        wayy += dist
    elif opp == 's':
        wayy -= dist
    elif opp == 'e':
        wayx += dist
    elif opp == 'w':
        wayx -= dist
    elif opp == 'l':
        angle = math.radians(dist)
        tx = wayx - shipx
        ty = wayy - shipy
        wayx = tx*math.cos(angle) - ty*math.sin(angle) + shipx
        wayy = tx*math.sin(angle) + ty*math.cos(angle) + shipy
    elif opp == 'r':
        angle = -math.radians(dist)
        tx = wayx - shipx
        ty = wayy - shipy
        wayx = tx*math.cos(angle) - ty*math.sin(angle) + shipx
        wayy = tx*math.sin(angle) + ty*math.cos(angle) + shipy
    elif opp == 'f':
        xd = wayx - shipx
        yd = wayy - shipy
        shipx += xd*dist
        shipy += yd*dist
        wayx += xd*dist
        wayy += yd*dist
        #x += dist*math.cos(math.radians(angle))
        #y += dist*math.sin(math.radians(angle))
    #print('Out', x, y, angle)
    print('After:')
    print('Ship pos:', shipx, ', ', shipy)
    print('Waypoint pos:', wayx, ', ', wayy)
    print('-'*10)
    return (shipx, shipy), (wayx, wayy)

ship = (0, 0)
waypoint = (10, 1)
for line in sys.stdin.readlines():
    line = line.strip()
    opp = line[0].lower()
    d = int(line[1:])
    ship, waypoint = move(ship, waypoint, opp, d)
print(ship)
print(int(abs(ship[0]) + abs(ship[1])))
