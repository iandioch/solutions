n = int(input())
print('{}:'.format(n))
for i in range(2, n):
    for j in range(max(i-1, 1), i+1):
        a = n//i
        for k in range(1, a+1):
            left = n - k*i
            if left % j != 0:
                continue
            b = left//j
            if k == b or k == b+1:
                print('{},{}'.format(i, j))

