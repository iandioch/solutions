def find_max(a, b, c):
    r = b/(2*a)
    return -a*r*r + b*r + c

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        best = -1
        best_v = 0
        for i in range(1, n+1):
            a, b, c = map(int, input().split())
            ans = find_max(a, b, c)
            if ans > best_v:
                best = i
                best_v = ans
        print(best)

if __name__ == '__main__':
    main()
