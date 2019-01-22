match = [-1]*10000
revmatch = [-1]*10000

def dfs(adj, curr, seen):
    seen[curr] = True
    for o in adj[curr]:
        if match[o] == -1 or (not seen[match[o]] and dfs(adj, match[o], seen)):
            match[o] = curr
            revmatch[curr] = o
            return True
    return False

def max_match(adj, nvert, nedge):
    for i in range(nvert):
        if revmatch[i] != -1:
            continue
        if not dfs(adj, i, [False]*nvert):
            return False
    return True

def main():
    nvert, nedge = map(int, input().split())
    adj = [[] for _ in range(nvert)]
    for _ in range(nedge):
        a, b = map(int, input().split())
        adj[a].append(b)
    ok = max_match(adj, nvert, nedge)
    print('YES' if ok else 'NO')

if __name__ == '__main__':
    main()
