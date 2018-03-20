t = int(input())
for _ in range(t):
    n = int(input()) + 1
    p = list(map(int, input().split()))
    m = int(input()) + 1
    q = list(map(int, input().split()))
    order = [0 for _ in range(n+m-1)]
    for i in range(n):
        for j in range(m):
            order[i+j] += p[i]*q[j]
    print(n+m-2)
    print(*order)
