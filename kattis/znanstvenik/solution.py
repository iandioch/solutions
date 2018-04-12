def check(num_to_delete, s, w, h):
    num = h - num_to_delete
    for i in range(len(s)-1):
        a = s[i][:num]
        b = s[i+1][:num]
        if a == b:
            return False
    return True

def main():
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]

    s = [[g[j][i] for j in range(h-1, -1, -1)] for i in range(w)]
    s.sort()

    lo = 0
    hi = h
    best = 0
    while True:
        if lo >= hi:
            break
        num_to_delete = (lo+hi)//2
        ok = check(num_to_delete, s, w, h)
        if ok:
            best = num_to_delete
            lo = num_to_delete + 1
        else:
            hi = num_to_delete

    print(best)

if __name__ == '__main__':
    main()
