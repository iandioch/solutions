def diff(seq):
    return [seq[i+1] - seq[i] for i in range(len(seq)-1)]

n, *v = list(map(int, input().split()))

w = [v]
ans = None
while True:
    x = diff(w[-1])
    y = sorted(x)
    if y[0] == y[-1]:
        ans = x[0]
        break
    else:
        w.append(x)
for i in range(len(w)-1, -1, -1):
    x = w[i]
    x.append(x[-1]+ans)
    ans = x[-1]
print(len(w), ans)
