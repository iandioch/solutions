def main():
    n = int(input())
    m = list(map(int, input().split()))
    m.sort()
    b = n
    for i, a in enumerate(m): 
        b = min(b, a + n - i - 1)
    print(b)

main()
