def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        d = {}
        p = []
        for _ in range(n):
            input() # pizza name
            _, *u = input().split()
            _, *v = input().split()
            u = set(u)
            v = set(v)
            for w in u:
                if w in d:
                    d[w] &= v
                else:
                    d[w] = set(v)
            p.append((u, v))
        for u, v in p:
            for w in d:
                if w not in u:
                    d[w] -= v
        ans = []
        for k in d:
            for o in d[k]:
                ans.append((k, o))
        ans.sort()
        for a in ans:
            print('({}, {})'.format(*a))
        print()

if __name__ == '__main__':
    main()
