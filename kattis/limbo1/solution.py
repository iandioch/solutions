def main():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        x = ((a+b) * (a+b+1))//2
        print(x + 1 + b)

if __name__ == '__main__':
    main()
