q = []
q.append(tuple(map(int, input().split())))
q.append(tuple(map(int, input().split())))
q.append(tuple(map(int, input().split())))
def area(p):
    return abs(p[0][0]*(p[1][1] - p[2][1]) + p[1][0]*(p[2][1] - p[0][1]) + p[2][0]*(p[0][1] - p[1][1]))/2
print('{:.1f}'.format(area(q)))

def sign(a, b, c):
    return (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])

def contains_point(x, y):
    v = (x, y)
    a = area((q[0], q[1], v))
    b = area((q[1], q[2], v))
    c = area((q[2], q[0], v))
    return abs(a+b+c - area(q)) < 0.00005

num = int(input())
ans = 0
for _ in range(num):
    x, y = map(int, input().split())
    if contains_point(x, y):
        ans += 1
print(ans)
