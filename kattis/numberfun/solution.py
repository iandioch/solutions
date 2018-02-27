n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b == c or a - b == c or b - a == c or a * c == b or b * c == a or a * b == c:
        print('Possible')
    else:
        print('Impossible')
