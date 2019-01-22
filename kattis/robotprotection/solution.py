def direction(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def graham_scan(pts):
    '''Given a list of points in the form [(x1, y1), (x2, y2), ...],
    return the convex hull in anticlockwise order starting with the lexicographically
    smallest point.'''
    # Remove duplicates
    pts = set(pts)
    n = len(pts)

    # Trivial case
    if n == 1:
        return pts

    pts = sorted(pts)

    U = []
    L = []
    for p in pts:
        while len(U) > 1 and direction(U[-2], U[-1], p) > 0:
            U.pop()
        while len(L) > 1 and direction(L[-2], L[-1], p) < 0:
            L.pop()
        L.append(p)
        U.append(p)
    H = L + U[1:-1][::-1]
    return H

def signed_shoelace(x, y, n):
    a, b = 0, 0
    for i in range(n-1):
        a += (x[i] * y[i+1])
        b += (y[i] * x[i+1])
    a += x[n-1] * y[0]
    b += y[n-1] * x[0]
    return (a-b)/2.0

def main():
    x = [0]*10001
    y = [0]*10001
    while True:
        n = int(input())
        if n == 0:
            return
        for i in range(n):
            x[i], y[i] = map(int, input().split())
        pts = graham_scan(zip(x[:n], y[:n]))
        i, j = zip(*pts)
        a = abs(signed_shoelace(i, j, len(pts)))
        print(a)


if __name__ == '__main__':
    main()
