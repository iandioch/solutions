def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def main():
    a, b = map(int, input().split('/'))
    a -= 32*b
    a *= 5
    b *= 9

    c = gcd(a, b)
    a //= c
    b //= c

    neg = (a < 0) != (b < 0)
    a = abs(a)
    b = abs(b)
    if neg:
        print('-{}/{}'.format(a, b))
    else:
        print('{}/{}'.format(a, b))

if __name__ == '__main__':
    main()
