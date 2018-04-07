MOD = 100000
OPEN_BRACKETS = '([{'
CLOSE_BRACKETS = ')]}'

n = int(input())
s = input().strip()

memo = {}


def mod(a):
    if a > MOD:
        return MOD + (a%MOD)
    else:
        return a


def solve(lo, hi):
    t = (lo, hi)
    if t in memo:
        return memo[t]
    if lo >= hi:
        return 1
    ans = 0
    for bracket in range(3):
        if s[lo] == OPEN_BRACKETS[bracket] or s[lo] == '?':
            for close in range(lo + 1, hi + 1, 2):
                if s[close] == CLOSE_BRACKETS[bracket] or s[close] == '?':
                    ans += solve(lo+1, close-1) * solve(close+1, hi)
                    ans = mod(ans)
    memo[t] = ans
    return ans


ans = (solve(0, n-1))
if ans < MOD:
    print(ans)
else:
    ans -= MOD
    for i in range(len(str(ans)), 5):
        print('0', end='')
    print(ans)
