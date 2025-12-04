def main():
    ans = 0
    id_ranges = input().split(',')
    for id_range in id_ranges:
        p, q = id_range.split('-')
        p = int(p)
        q = int(q)
        for i in range(p, q+1):
            s = str(i)
            if len(s) % 2 == 1:
                continue
            if s[:len(s)//2] == s[len(s)//2:]:
                ans += i
    print(ans)

main()
