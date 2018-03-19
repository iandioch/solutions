def is_prime(n):
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

while True:
    p, a = map(int, input().split())
    if a == p == 0:
        break
    print(a**p, (a**p)%p, a%p)
    r = pow(a, p, p)
    if r == a and not is_prime(p):
        print('yes')
    else:
        print('no')
