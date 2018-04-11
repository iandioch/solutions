POWS = [1]
while POWS[-1] < 10**9:
    POWS.append(POWS[-1]*2)
POWS = set(POWS)

def solve(n):
    if n in POWS:
        print('IMPOSSIBLE')
        return
    v = 2
    m = 2*n
    start = None
    ok = False
    while v*v <= m + 1:
        if m % v == 0 and (((m//v) - v) % 2) == 1:
            start = ((2*n)//v - v + 1)//2
            if start > 0:
                ok = True
                break
        v += 1

    if ok:
        print(n, '=', ' + '.join(str(c) for c in range(start, start+v)))
        return
    print('IMPOSSIBLE')

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        solve(m)

if __name__ == '__main__':
    main()

