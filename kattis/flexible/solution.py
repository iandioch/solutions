w, n = map(int, input().split())
m = list(map(int, input().split())) + [w]
s = set(m)
for i in range(n):
    for j in range(i+1, n+1):
        s.add(m[j]-m[i])

print(' '.join([str(c) for c in sorted(s)]))
