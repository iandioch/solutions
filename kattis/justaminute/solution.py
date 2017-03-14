i, j = 0, 0
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a *= 60
    i += a
    j += b
if j/i <= 1:
    print('measurement error')
else:
    print('{:.8f}'.format(j/i))
