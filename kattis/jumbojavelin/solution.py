n = int(input())
f = list(map(int, (input() for _ in range(n))))
print(sum(f) - len(f) + 1)
