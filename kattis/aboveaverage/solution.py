t = int(input())
for _ in range(t):
    n, *s = map(int, input().split())
    avg = sum(s)/n
    a = len([i for i in s if i > avg])
    print('{:.3f}%'.format(100*a/n))
