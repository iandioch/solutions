from sys import stdin

def direction(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def graham_scan(pts):
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

def main():
    read = stdin.readline
    n = int(read())
    pts = []
    for _ in range(n):
        a, b, c = read().split()
        if c == 'Y':
            pts.append((int(a), int(b)))
    ans = graham_scan(pts)
    print(len(ans))
    for p in ans:
        print(*p)

if __name__ == '__main__':
    main()
