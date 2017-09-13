def is_arithmetic(v):
    d = v[1] - v[0]
    for i in range(1, len(v)-1):
        if v[i+1] - v[i] != d:
            return False
    return True

n = int(input())
for _ in range(n):
    v = list(map(int, input().split()[1:]))
    if is_arithmetic(v):
        print('arithmetic')
    elif is_arithmetic(sorted(v)):
        print('permuted arithmetic')
    else:
        print('non-arithmetic')
