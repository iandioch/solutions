def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def reduce_fraction(num, denom):
    g = gcd(num, denom)
    return num//g, denom//g

def add_fraction(n1, d1, n2, d2):
    n = (n1*d2) + (n2*d1)
    d = d1 * d2
    return reduce_fraction(n, d)

def main():
    n = int(input())
    c = list(map(int, input().split()))


    num = 0
    denom = 1
    for v in c[::-1]:
        num, denom = add_fraction(v, 1, num, denom)
        num, denom = denom, num
    num, denom = denom, num
    print('{}/{}'.format(num, denom))
main()
