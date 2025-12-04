import sys

memo = {}

def dp(bank, index, rem):
    if index >= len(bank):
        return -100000000000000

    if rem == 1:
        return max(bank[index:])
    if rem == 0:
        return 0

    k = (index, rem)
    if k in memo:
        return memo[k]

    n = bank[index] * (10**(rem-1))
    memo[k] = max(n + dp(bank, index+1, rem-1), dp(bank, index+1, rem))
    return memo[k]

def bank_joltage(bank):
    global memo
    memo = {}
    return dp(bank, 0, 12)

def main():
    ans = 0
    for line in sys.stdin.readlines():
        bank = list(map(int, line.strip()))
        j = bank_joltage(bank)
        print(j, line)
        ans += j
    print(ans)

main()
