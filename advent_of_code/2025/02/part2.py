def is_repeated(s, n):
    if len(s) % n != 0:
        return False
    t = s[:n]
    for i in range(len(s)//n):
        u = s[i*n:i*n + n]
        if t != u:
            return False
    return True

def main():
    ans = 0
    id_ranges = input().split(',')
    for id_range in id_ranges:
        p, q = id_range.split('-')
        p = int(p)
        q = int(q)
        for i in range(p, q+1):
            s = str(i)
            valid = True
            for n in range(1, len(s) // 2 + 1):
                if is_repeated(s, n):
                    valid = False
                    break
            if not valid:
                ans += i
    print(ans)

main()
