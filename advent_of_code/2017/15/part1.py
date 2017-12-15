PREFIX = '0'*16

def getbin(c):
    s = PREFIX + bin(c)[2:]
    return s[-16:]

a = int(input().split()[-1])
b = int(input().split()[-1])

ans = 0
for step in range(40000000):
    a = a*16807 % 2147483647
    b = b*48271 % 2147483647
    if getbin(a) == getbin(b):
        ans += 1

print(ans)
