numtests = int(input())

for test in range(1, numtests+1):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()), reverse=True)
    tot = 0
    for i in range(n):
        tot += a[i]*b[i]
    print('Case #{}: {}'.format(test, tot))
