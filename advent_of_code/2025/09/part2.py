import sys

from collections import deque

def flood_fill(t):
    def _fill_from(m, n):
        q = deque([(m, n)])
        while len(q):
            a, b = q.popleft()
            if a < 0 or b < 0 or a >= len(t[0]) or b >= len(t):
                continue
            if t[b][a]:
                continue
            t[b][a] = True
            q.append((a-1, b))
            q.append((a+1, b))
            q.append((a, b-1))
            q.append((a, b+1))

    for j in range(len(t)):
        for i in range(len(t[0])):
            if t[j][i]:
                _fill_from(i+1, j+1)
                return

def is_valid(t, a, b, x, y):
    for p in range(min(a, x), max(a, x)):
        for q in range(min(b, y), max(b, y)):
            if not t[q][p]:
                return False
    return True

def area(a, b, x, y):
    return (1+abs(a-x))*(1+abs(b-y))

def main():
    g = []
    for line in sys.stdin.readlines():
        a, b = map(int, line.strip().split(','))
        g.append((a, b))

    xsorted = sorted([p[0] for p in g])
    ysorted = sorted([p[1] for p in g])

    xi_to_x = {i:xsorted[i] for i in range(len(xsorted))}
    x_to_xi = {xsorted[i]:i for i in range(len(xsorted))}
    yi_to_y = {i:ysorted[i] for i in range(len(ysorted))}
    y_to_yi = {ysorted[i]:i for i in range(len(ysorted))}

    gi = [(x_to_xi[p[0]], y_to_yi[p[1]]) for p in g]
    print(gi)

    maxx = max(f[0] for f in gi) + 1
    maxy = max(f[1] for f in gi) + 1
    t = [[False for _ in range(maxx)] for _ in range(maxy)]
    for i in range(len(gi)):
        a, b = gi[i]
        t[b][a] = True
        # This will access element -1 when i == 0, as we want.
        x, y = gi[i-1]

        for p in range(min(a, x), max(a, x)+1):
            for q in range(min(b, y), max(b, y)+1):
                t[q][p] = True

    flood_fill(t)

    print(' ', ''.join('{:2d}'.format(i) for i in range(len(t[0]))))
    for i, row in enumerate(t):
        print(i, ''.join('X' if c else '.' for c in row[:len(row)//2]))

    ans = 0
    for i in range(len(g)-1):
        a, b = gi[i]
        for j in range(i+1, len(g)): 
            x, y = gi[j]

            poss = area(xi_to_x[a],yi_to_y[b],xi_to_x[x],yi_to_y[y])
            if poss < ans:
                continue
            print(f'Testing {i}-{j} (out of {len(g)}), area {poss}, best {ans}')
            if is_valid(t, a, b, x, y):
                print('Valid square:', a, b, x, y,poss)
                ans = max(ans, poss)
    print(ans)

main()
