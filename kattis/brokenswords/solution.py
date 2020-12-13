n = int(input())
tb, lr = 0, 0
for _ in range(n):
    s = [int(c) - 1 for c in input()]
    tb -= s[0]
    tb -= s[1]
    lr -= s[2]
    lr -= s[3]

tot = 0
while tb >= 2 and lr >= 2:
    tb -= 2
    lr -= 2
    tot += 1
print(tot, tb, lr)
