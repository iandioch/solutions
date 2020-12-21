import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

def main():
    x, y, x1, y1, x2, y2 = map(int, input().split())
    minn = 100000000
    for i in [x1, x2]:
        for j in [y1, y2]:
            e = dist(x, y, i, j)
            minn = min(minn, e)
    # If the goat is directly next to the house, so the dist is the shortest
    # straight-line dist.
    if x1 <= x <= x2:
        minn = min(minn, dist(x, y, x, y1))
        minn = min(minn, dist(x, y, x, y2))
    if y1 <= y <= y2:
        minn = min(minn, dist(x, y, x1, y))
        minn = min(minn, dist(x, y, x2, y))
    print(minn)

main()
