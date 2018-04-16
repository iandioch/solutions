DIGS = '0123456789ACDEFHJKLMNPRTVWX'
DIG_VALS = {v:i for i, v in enumerate(DIGS)}

def solve(s):
    t = [DIG_VALS[c] for c in s]
    u, check = t[:-1], t[-1]
    parity = 2*u[0] + 4*u[1] + 5*u[2] + 7*u[3] + 8*u[4] + 10*u[5] + 11*u[6] + 13*u[7]
    parity %= 27
    if parity != check:
        return 'Invalid'
    ans = 0
    for d in u:
        ans *= 27
        ans += d
    return ans

def main():
    n = int(input())
    for _ in range(n):
        m, s = input().split()
        ans = solve(s)
        print(m, ans)

if __name__ == '__main__':
    main()
