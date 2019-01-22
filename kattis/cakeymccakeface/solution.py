from collections import defaultdict

def main():
    n = int(input())
    m = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    d = defaultdict(int)

    for i in a:
        for j in b:
            if i <= j:
                d[j-i] += 1
    x = sorted(d)
    x = sorted(x, key = lambda y: -d[y])
    if len(x):
        print(x[0])
    else:
        print(0)


if __name__ == '__main__':
    main()
