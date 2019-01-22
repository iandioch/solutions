import collections
import sys

def dfs(been, curr, routes, memo={}):
    if curr in memo:
        return memo[curr]
    for other in routes[curr]:
        if other in been or dfs(been | {other}, other, routes):
            memo[other] = True
            return True
    memo[curr] = False
    return False

def contains_loop(start, routes):
    return dfs({start}, start, routes)

def main():
    lines = [s.strip() for s in sys.stdin.readlines()]
    n = int(lines[0])
    routes = collections.defaultdict(list)
    for i in range(1, n+1):
        a, b = lines[i].split()
        routes[a].append(b)
    for i in range(n+1, len(lines)):
        ok = contains_loop(lines[i], routes)
        print(lines[i], 'safe' if ok else 'trapped')

if __name__ == '__main__':
    main()
