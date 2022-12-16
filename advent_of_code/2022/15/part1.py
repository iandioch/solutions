import sys


def main():
    DESY = 2000000
    minx, miny = 100, 100
    maxx, maxy = 0, 0
    seen = set()
    sensor = set()
    beacon = set()

    def pp():
        for y in range(miny, maxy+1):
            s = [str(y)+'\t']
            for x in range(minx, maxx+1):
                p = (x, y)
                if p in sensor:
                    s.append('S')
                elif p in beacon:
                    s.append('B')
                elif p in seen:
                    s.append('#')
                else:
                    s.append('.')
            print(''.join(s))

    for line in sys.stdin.readlines():
        p = line.strip().split()
        sx, sy, bx, by = (int(f.split('=')[1].strip(',:')) for f in (p[2], p[3], p[-2], p[-1]))
        print('sensor', sx, sy, 'beacon', bx, by)
        d = abs(sx-bx) + abs(sy-by)
        minx = min(minx, sx-d, bx+d)
        maxx = max(maxx, sx-d, bx+d)
        miny = min(miny, sy-d, by+d)
        maxy = max(maxy, sy-d, by+d)
        sensor.add((sx, sy, d))
        beacon.add((bx, by))
    print(minx, maxx, miny, maxy)

    ans = 0
    for x in range(minx, maxx+1):
        found = False
        for bx, by in beacon:
            if bx == x and by == DESY:
                found = True
                break
        if found:
            continue
        for sx, sy, d in sensor:
            if abs(sx-x) + abs(sy-DESY) <= d:
                found = True
                break
        if found:
            ans += 1

    print(ans)

main()
