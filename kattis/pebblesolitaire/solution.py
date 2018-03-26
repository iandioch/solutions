d = {}

def get_num(a):
    at = tuple(a)
    if at in d:
        return d[at]
    ans = sum(a)
    for i in range(10):
        if not a[i] and a[i+1] and a[i+2]:
            b = list(a)
            b[i] = True
            b[i+1] = False
            b[i+2] = False
            ans = min(ans, get_num(b))
    for i in range(2, 12):
        if not a[i] and a[i-1] and a[i-2]:
            b = list(a)
            b[i] = True
            b[i-1] = False
            b[i-2] = False
            ans = min(ans, get_num(b))
    d[at] = ans
    return ans


n = int(input())
for _ in range(n):
    a = list(c == 'o' for c in input())
    print(get_num(a))
