n, m = map(int, input().split())
items = set(input().split())
for _ in range(n-1):
    items &= set(input().split())

print(len(items))
print('\n'.join(sorted(items)))
