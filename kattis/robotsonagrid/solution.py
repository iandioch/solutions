MOD = 2**31 - 1

n = int(raw_input())
g = [[(c == '.') for c in raw_input().strip()] for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]
ans[0][0] = 1
for i in range(1, n):
    if g[0][i]:
        ans[0][i] = ans[0][i-1]
    if g[i][0]:
        ans[i][0] = ans[i-1][0]

for i in range(1, n):
    for j in range(1, n):
        if g[i][j]:
            ans[i][j] = (ans[i-1][j] + ans[i][j-1]) % MOD

if ans[-1][-1] == 0:
    # figure out if connected at all
    q = [(0,0)]
    visited = set()
    qi = 0
    while qi < len(q):
        i, j = q[qi]
        qi += 1
        if (i, j) in visited:
            continue
        if not g[i][j]:
            continue
        visited.add((i,j))
        if i > 0 and (i-1,j) not in visited:
            q.append((i-1,j))
        if j > 0 and (i,j-1) not in visited:
            q.append((i,j-1))
        if i < n-1 and (i+1,j) not in visited:
            q.append((i+1,j))
        if j < n-1 and (i,j+1) not in visited:
            q.append((i,j+1))
    if (n-1, n-1) in visited:
        print('THE GAME IS A LIE')
    else:
        print('INCONCEIVABLE')
else:
    print(ans[-1][-1])
