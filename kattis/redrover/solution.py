s = input()
b = len(s)
for i in range(len(s)-1):
    for j in range(i+1, len(s)):
        m = s[i:j]
        t = s.replace(m, 'm')
        v = len(t) + len(m)
        b = min(b, v)
print(b)
