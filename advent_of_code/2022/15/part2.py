import sys


def main():
    MAXP = 4000000
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

    def check_row(y, left, right):
        ranges = []
        for sx, sy, d in sensor:
            minx = sx - d + abs(sy-y)
            maxx = sx + d - abs(sy-y)
            """
            foundmin = False
            for x in range(sx-d, sx+d+1):
                if abs(sx-x) + abs(sy-y) <= d:
                    foundmin = True
                    maxx = x
                    continue

                if foundmin:
                    break
                else:
                    minx = x
            minx += 1
            if maxx <= minx:
                continue"""
            ranges.append((minx, maxx))
            #print('sensor at', sx, sy, 'can see', ranges[-1])
        ranges_start = sorted(ranges[:])
        ranges_end = sorted(ranges[:], key=lambda x:x[1])
        #print('row', y, 'ranges:', ranges)
        while True:
            merged = False
            for i in range(len(ranges)-1):
                for j in range(i+1, len(ranges)):
                    def merge():
                        nonlocal merged
                        ranges.append((min(ranges[i][0], ranges[j][0]), max(ranges[i][1], ranges[j][1])))
                        #print('merging', ranges[i], 'and', ranges[j], 'into', ranges[-1])
                        del ranges[j]
                        del ranges[i]
                        merged = True
                    if ranges[i][0] >= ranges[j][0] and ranges[i][1] <= ranges[j][1]:
                        # i is entirely inside j
                        merge()
                        break
                    if ranges[j][0] >= ranges[i][0] and ranges[j][1] <= ranges[i][1]:
                        # j is entirely inside i
                        merge()
                        break
                    if ranges[i][0] >= ranges[j][0] and ranges[i][0] <= ranges[j][1]:
                        merge()
                        break
                    if ranges[i][1] >= ranges[j][0] and ranges[i][1] <= ranges[j][1]:
                        merge()
                        break
                    if ranges[i][0] < ranges[j][0] and ranges[i][1] >= ranges[j][0]-1:
                        merge()
                        break
                if merged:
                    break
            if not merged:
                if len(ranges) > 1:
                    print('IN ROW', y, ', NOT MERGED:', ranges)
                    # whatever is printed here, I just manually got the X
                    # from outside the printed ranges, mult'd it by 4m,
                    # and added y
                    return True
                break


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

    ans = 0
    for y in range(0, MAXP+1):
        if y % 10000 == 0:
            print('checking', y)
        if check_row(y, 0, MAXP+1):
            break

main()
