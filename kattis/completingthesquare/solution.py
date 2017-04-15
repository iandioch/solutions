from math import sqrt, acos

def dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def angle(a, b, c):
    # get angle at a between b and c
    n = (dist(a, b)**2 + dist(a, c)**2 - dist(b, c)**2)
    d = 2*dist(a, b)*dist(a, c)
    return (acos(n/d))

d = [tuple(map(int, input().split())) for _ in range(3)]

for i in range(-3, 0):
    if angle(d[i], d[i+1], d[i+2]) > 1:
        # there is a right angle at d[i] between lines towards
        # points d[i+1] and d[i+2]
        # the 4th point of the square will be at the point if
        # we transform d[i+2] by d[i]->d[i+1]
        x = d[i+2][0] + (d[i+1][0] - d[i][0])
        y = d[i+2][1] + (d[i+1][1] - d[i][1])
        print(x, y)
        break
