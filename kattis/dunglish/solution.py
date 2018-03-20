from collections import defaultdict
correct = defaultdict(int)
incorrect = defaultdict(int)

trans = {}

input()
sentence = input().strip().split()
n = int(input())
for _ in range(n):
    d, e, corr = input().split()
    trans[d] = e
    if corr == 'correct':
        correct[d] += 1
    else:
        incorrect[d] += 1

tot = 1
ok = 1
for word in sentence:
    ok *= correct[word]
    tot *= (correct[word] + incorrect[word])

if tot == 1:
    print(' '.join(trans[s] for s in sentence))
    if ok == 0:
        print('incorrect')
    else:
        print('correct')
else:
    print(ok, 'correct')
    print(tot-ok, 'incorrect')
