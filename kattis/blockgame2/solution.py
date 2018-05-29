'Returns True if win, False if lose'
def bop(a, b):
    if a == 1:
        return True
    if b % a == 0:
        return True
    if b > 2*a:
        return True
    return not bop(b-a, a)


def main():
    a, b = map(int, input().split())
    z = bop(min(a, b), max(a, b))
    if z:
        print('win')
    else:
        print('lose')

main()
