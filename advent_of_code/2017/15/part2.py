MAX = 5000000
PREFIX = '0'*16

def getbin(c):
    s = PREFIX + bin(c)[2:]
    return s[-16:]

a = int(input().split()[-1])
b = int(input().split()[-1])

ad = []
bd = []

ans = 0
while True:
    a = a*16807 % 2147483647
    b = b*48271 % 2147483647

    if a % 4 == 0:
        ad.append(a)
        if len(ad) > MAX and len(bd) > MAX:
            break
    if b % 8 == 0:
        bd.append(b)
        if len(ad) > MAX and len(bd) > MAX:
            break

for i in range(MAX):
    if getbin(ad[i]) == getbin(bd[i]):
        ans += 1

print(ans)
