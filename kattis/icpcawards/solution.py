used = set()

i = 0
n = int(input())
for _ in range(n):
    uni, team = input().split()
    if i >= 12 or uni in used:
        continue
    i += 1
    used.add(uni)
    print(uni, team)
