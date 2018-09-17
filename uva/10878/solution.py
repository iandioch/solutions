def main():
    ans = ''
    input()
    while True:
        s = input()
        if s[1] == '_':
            break
        s = s.replace('o', '1').replace(' ', '0').replace('.', '')[1:-1]
        n = int(s, 2)
        ans += chr(n)
    print(ans, end='')

if __name__ == '__main__':
    main()
