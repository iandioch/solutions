import sys
import math

def dist(x, y, i, j):
    return math.sqrt((x - i)*(x - i) + (y - j)*(y - j))

def main():
    cx, cy, n = map(int, sys.stdin.readline().split())

    v = []
    d = []

    for line in sys.stdin.readlines():
        x, y, r = map(int, line.split())
        v.append((x, y, r))
        d.append(dist(cx, cy, x, y) - r)

    d.sort()

    if d[2] < 0:
        print(0)
    else:
        print(math.floor(d[2]))

if __name__ == '__main__':
    main()
