s = input().strip()
n = len(s)

h, w = 0, 0
for i in range(n-1, 0, -1):
    h = i
    w = (n//h)
    if h > w:
        continue
    if h*w == n:
        break

t = [[] for _ in range(h)]
k = 0
for i in range(w):
    for j in range(h):
        t[j].append(s[k])
        k += 1
for u in t:
    print(''.join(u), end='')
