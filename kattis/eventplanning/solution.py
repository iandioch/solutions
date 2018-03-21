n, budget, hotels, weeks = map(int, input().split())
best = None
for _ in range(hotels):
    c = int(input())
    for w in map(int, input().split()):
        if w >= n:
            b = c*n
            if not best or b < best:
                best = b
            break
if not best or best > budget:
    print('stay home')
else:
    print(best)
