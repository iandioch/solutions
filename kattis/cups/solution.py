n = int(input())

digs = set('0123456789')
cols = {}

for i in range(n):
    parts = input().split()
    if all([c in digs for c in parts[0]]):
        cols[parts[1]] = int(parts[0])//2
    else:
        cols[parts[0]] = int(parts[1])

print('\n'.join(sorted(cols, key=lambda x: cols[x])))
