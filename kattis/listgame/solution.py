n = int(input())

ans = 0
while n % 2 == 0:
    n /= 2
    ans += 1
a = 3
m = n
while a*a <= n:
    while a*a <= n and m % a > 0:
        a += 2
    if m % a != 0:
        break
    m //= a
    ans += 1
if m > 1:
    ans += 1
print(ans)    
