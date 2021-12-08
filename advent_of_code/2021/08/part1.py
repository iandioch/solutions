import sys

def main():
    ans = 0
    for line in sys.stdin.readlines():
        parts = [part.strip().split() for part in line.split('|')]
        for num in parts[1]:
            if len(num) in [2, 3, 4, 7]:
                ans += 1

    print(ans)

main()
