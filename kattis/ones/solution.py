import sys

def main():
    for line in sys.stdin:
        p = int(line)
        d = 1%p
        ans = 1
        while d:
            d = (d*10+1)%p
            ans += 1
        print(ans)

if __name__ == '__main__':
    main()
