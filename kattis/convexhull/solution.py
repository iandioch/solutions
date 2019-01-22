from sys import stdin

def clockwise(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1) > 0

def graham_scan(pts):
    # Remove duplicates
    pts = set(pts)
    n = len(pts)

    # Trivial case
    if n <= 2:
        return pts

    pts = sorted(pts)
    U = [pts[0], pts[1]] # upper hull
    L = [pts[-1], pts[-2]] # lower hull

    for i in range(2, n):
        while len(U) > 1 and not clockwise(pts[i], U[-1], U[-2]):
            U.pop()
        U.append(pts[i])
    for i in range(n-2, -1, -1):
        while len(L) > 1 and not clockwise(pts[i], L[-1], L[-2]):
            L.pop()
        L.append(pts[i])

    H = U[:-1] + L[:-1]
    H = H[::-1]
    return H

def main():
    read = stdin.readline
    while True:
        n = int(read())
        if n == 0:
            break
        pts = [tuple(map(int, read().split())) for _ in range(n)]
        ans = graham_scan(pts)
        print(len(ans))
        for x, y in ans:
            print(x, y)

if __name__ == '__main__':
    main()
