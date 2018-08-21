from collections import defaultdict

def main():
    n = int(input())

    d = defaultdict(int)
    e = defaultdict(set)
    names = set()
    for _ in range(n):
        name, *s = input().split()
        names.add(name)
        for t in s:
            e[t].add(name) 
            d[t] += 1
    ni = len(names)
    p = sorted([w for w in d if len(e[w]) == ni], key = lambda x: (-d[x], x))
    if len(p):
        print('\n'.join(p))
    else:
        print('ALL CLEAR')

if __name__ == '__main__':
    main()
