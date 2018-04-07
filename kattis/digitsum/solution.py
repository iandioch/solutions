memo = {}

def digit_sum(n):
    ans = 0
    while n > 0:
        ans += n%10
        n //= 10
    return ans

def count(n):
    if n <= 0:
        return 0
    if n % 10 == 0:
        # 1+2+3+4+5+6+7+8+9 = 45
        ans = 10 * count(n//10) + 45*(n//10)
        memo[n] = ans
        return ans
    ans = count(n-1) + digit_sum(n-1)
    memo[n] = ans
    return ans

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(count(b+1) - count(a))
