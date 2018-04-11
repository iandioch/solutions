def req(n, arr):
    while n > 0:
        a = n % 10
        arr[a] += 1
        n //= 10

t = int(input())

for _ in range(t):
    addr = input()
    print(addr)
    p = input().split()
    print(*p)
    n = int(p[0])
    m = 0
    ans = [0 for _ in range(10)]
    while m < n:
        p = input()
        if p[0] == '+':
            p = p.split()
            start = int(p[1])
            end = int(p[2])
            inc = int(p[3])
            for x in range(start, end+1, inc):
                req(x, ans)
                m += 1
        else:
            req(int(p), ans)
            m += 1
    tot = 0
    for i in range(10):
        print('Make', ans[i], 'digit', i)
        tot += ans[i]
    dig = 'digit'
    if tot > 1:
        dig += 's'
    print('In total', tot, dig)
