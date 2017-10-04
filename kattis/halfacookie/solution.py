import sys
from math import *

for line in sys.stdin.readlines():
    r, x, y = map(float, line.split())
    d = (x**2 + y**2)**0.5
    if d > r:
        print('miss')
        continue
    circle_area = pi * (r**2)
    theta = 2*acos(d/r)
    segment_area = (r**2)*(theta - sin(theta))/2
    print(circle_area - segment_area, segment_area)
