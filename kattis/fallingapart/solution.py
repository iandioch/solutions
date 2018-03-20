n = int(input())
s = sorted(map(int, input().split()), reverse=True)
print(sum(s[::2]), sum(s[1::2]))
