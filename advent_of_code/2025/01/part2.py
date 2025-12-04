import sys

def main():
    ans = 0
    dial = 50
    for line in sys.stdin.readlines():
        line = line.strip()
        d, n = line[0], int(line[1:])
        if d == 'L':
            direction = -1
        else:
            direction = 1

        for i in range(dial, dial + n*direction, direction):
            if (i%100) == 0:
                ans += 1
        dial += n * direction
    print(ans)

main()
