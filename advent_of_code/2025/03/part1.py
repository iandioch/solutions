import sys

def bank_joltage(bank):
    best = 0
    jolts = 0
    for i in bank:
        if_second = best * 10 + i
        jolts = max(jolts, if_second)
        if i > best:
            best = i
    return jolts

def main():
    ans = 0
    for line in sys.stdin.readlines():
        bank = list(map(int, line.strip()))
        ans += bank_joltage(bank)
    print(ans)

main()
