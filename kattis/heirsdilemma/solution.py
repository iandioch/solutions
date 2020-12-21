def main():
    l, h = map(int, input().split())
    ans = 0
    for i in range(l, h+1):
        digs = str(i)
        if len(set(digs)) != 6:
            # Digits non-unique
            continue
        if '0' in digs:
            continue
        div = True
        for c in digs:
            if i % int(c) != 0:
                div = False
                break
        if not div:
            continue
        ans += 1
    print(ans)

main()
