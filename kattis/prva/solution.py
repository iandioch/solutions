h, w = map(int, input().split())
lines = [input() for _ in range(h)]
word = 'zzzzzzzzzzzzzzzz'
for line in lines:
    a = line.split('#')
    for b in a:
        if len(b) >= 2:
            if b < word:
                word = b

for i in range(w):
    s = ''.join([lines[j][i] for j in range(h)])
    a = s.split('#')
    for b in a:
        if len(b) >= 2:
            if b < word:
                word = b

print(word)
