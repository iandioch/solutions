t = int(input())

for test in range(1, t+1):

    n, a, b, c, d, x, y, m = map(int, input().split())

    pts = [[0 for _ in range(3)] for _ in range(3)]
    for _ in range(n):
        pts[x%3][y%3] += 1
        x = (a*x + b) % m
        y = (c*y + d) % m

    ans = 0

    for a in range(9):
        i = a % 3
        j = a // 3
        if pts[i][j] >= 3:
            ans += (pts[i][j] * (pts[i][j] - 1) * (pts[i][j] - 2)) // 6
        okFor2 = pts[i][j] >= 2
        for b in range(a+1, 9):
            k = b % 3
            l = b // 3
            if okFor2 and ((i + i + k) % 3) == 0 and ((j + j + l) % 3) == 0:
                ans += (pts[i][j] * (pts[i][j] - 1) * (pts[k][l])) // 2
            for c in range(b+1, 9):
                m = c % 3
                n = c // 3
                if ((i + k + m) % 3) == 0 and ((j + l + n) % 3) == 0:
                    ans += pts[i][j] * pts[k][l] * pts[m][n]


    print('Case #{}: {}'.format(test, ans))
