N = 10**12

def can_get_count(n, s, parts=2):
    if n <= 0:
        return False
    if parts > len(s):
        return False
    if int(s) == n:
        return True
    for i in range(1, len(s)):
        p = int(s[:i])
        t = s[i:]
        remainder = n - p
        if int(t) + p == n:
            return True
        if can_get_count(remainder, t):
            return True
    return can_get_count(n, t, parts+1)

def is_s_num(n, ro):
    return can_get_count(ro, str(n))

def main():
    squares = {}
    i = 1
    while True:
        sq = i*i
        if sq > N:
            break
        squares[sq] = i
        i += 1
    tot = 0
    print(is_s_num(81, 9))
    g = 0
    for s in sorted(squares):
        rem = s % 9
        if rem > 1:
            # OEIS A038206 tells me these are all congruent to 0 or 1 mod 9
            continue
        if is_s_num(s, squares[s]):
            g += 1
            tot += s
            print(f'{g}: {s} (running total: {tot}')
    print(tot)



if __name__ == '__main__':
    main()
