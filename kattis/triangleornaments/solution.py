import math

def angle(a, b, c):
    # Get angle opposite to side a

    cosA = (b*b + c*c - a*a)/(2*b*c)
    return math.acos(cosA)

def width(a, b, c):
    a_ang = angle(a, b, c)
    b_ang = angle(b, c, a)

    # points of triangle
    A = (-a*math.cos(b_ang), a*math.sin(b_ang))
    B = (b*math.cos(a_ang), b*math.sin(a_ang))
    C = (0, 0)
    centroid_x = sum(x[0] for x in (A, B, C))/3
    centroid_y = sum(x[1] for x in (A, B, C))/3

    ang = math.atan2(centroid_y, centroid_x)
    ang -= math.pi/2
    return c*math.cos(ang)

def main():
    tot = 0
    n = int(input())
    for _ in range(n):
        a, b, c = map(float, input().split())
        tot += width(a, b, c)
    print(tot)

if __name__ == '__main__':
    main()
