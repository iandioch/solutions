import sys

def main():
    ans = 0
    for line in sys.stdin.readlines():
        a, b = line.strip().split(',')
        i, j = map(int, a.split('-'))
        p, q = map(int, b.split('-'))
        if j < p or q < i:
            continue 
        ans += 1
    print(ans)

main()
