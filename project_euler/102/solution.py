import sys

lines = sys.stdin.readlines()

triangles = []

num = 0
for line in lines:
    x0, y0, x1, y1, x2, y2 = [int(x) for x in line.split(',')]
    
    
    # with help from from http://stackoverflow.com/a/14382692
    px, py = 0, 0
    area = 1.0/2*(-y1*x2 + y0*(-x1 + x2) + x0*(y1 - y2) + x1*y2)
    s = 1/(2*area)*(y0*x2 - x0*y2 + (y2-y0)*px + (x0 - x2)*py)
    t = 1/(2*area)*(x0*y1 - y0*x1 + (y0-y1)*px + (x1 - x0)*py)
    if s > 0 and t > 0 and 1 - s - t > 0:
        num += 1

print num
