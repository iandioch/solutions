d = {
    "Adrian": "ABC",
    "Bruno": "BABC",
    "Goran": "CCAABB"
}

n = int(input())
correct = input()
best = 0
best_boy = []
for e in d:
    choices = d[e]
    f = 0
    for c in range(n):
        if correct[c] == choices[c%len(choices)]:
            f += 1
    if f == best:
        best_boy.append(e)
    elif f > best:
        best = f
        best_boy = [e]

print(best)
print('\n'.join(sorted(best_boy)))
