import sys

def main():
    ans = 0
    dial = 50
    for line in sys.stdin.readlines():
        d, n = line[0], int(line[1:])
        if d == 'L':
            dial -= n
        else:
            dial += n
        dial %= 100
        if dial == 0:
            ans += 1
    print(ans)

main()
