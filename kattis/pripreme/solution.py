input()
d = list(map(int, input().split()))
a = sum(d)
b = max(d)
if b > (a-b):
    print(b*2)
else:
    print(a)
