def main():
    n = int(input())
    for _ in range(n):
        d = int(input())
        d -= 1
        a = (8 * pow(9, d, 1000000007)) % 1000000007
        print(a)

main()
