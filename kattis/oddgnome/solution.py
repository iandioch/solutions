t = int(input())
for _ in range(t):
    _, *g = list(map(int, input().split()))
    for i in range(1, len(g) - 1):
        if g[i] != g[i-1]+1:
            print(i+1)
            break
