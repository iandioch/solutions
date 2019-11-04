def main():
    n = int(input())
    v = list(map(int, input().split()))
    k = [(m, i) for i, m in enumerate(v)]
    k.sort()
    print('1', end=' ')
    for d in k:
        print(d[1] + 2, end=' ')
    print()

main()
