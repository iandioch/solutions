from sys import stdin

def main():
    read = stdin.readline
    w = int(read())
    n = int(read())
    tot = 0
    for _ in range(n):
        a = [int(x) for x in read().split()]
        tot += a[0]*a[1]

    print(tot//w)

if __name__ == '__main__':
    main()
