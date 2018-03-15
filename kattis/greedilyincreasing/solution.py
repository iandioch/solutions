input()
s = list(map(int, input().split()))

a = [s[0]]
for c in s[1:]:
    if c > a[-1]:
        a.append(c)

print(len(a))
print(*a)
