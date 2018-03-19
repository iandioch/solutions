probs, tests = map(int, input().split())
tot = 0
for _ in range(probs):
    s = [input().strip() for _ in range(tests)]
    if all(t[0].lower() + t[1:] == t.lower() for t in s):
        tot += 1

print(tot)
