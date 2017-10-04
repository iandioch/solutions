n = int(input())
lines = [input() for _ in range(n)]
print(len([s for s in lines if 'CD' not in s]))
