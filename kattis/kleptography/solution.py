def main():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    n, m = map(int, input().split())
    last = input()
    b = input()

    a = list(' '*(m-n) + last)
    for i in range(m-1, n-1, -1):
        a[i-n] = chr(ord('a') + (26 + ord(b[i]) - ord(a[i])) % 26)
    print(''.join(a))

main()
