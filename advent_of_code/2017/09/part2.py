i = 0
s = input()
junk = False
junk_score = 0
stack = []
score = 0
while i < len(s):
    if s[i] == '!':
        i += 2
        continue
    if junk:
        if s[i] == '>':
            junk = False
            score += junk_score
        else:
            junk_score += 1
        i += 1
        continue
    if s[i] == '<':
        junk_score = 0
        junk = True
        i += 1
        continue
    if s[i] == '{':
        stack.append(i)
        i += 1
        continue
    if s[i] == '}':
        stack.pop()
        i += 1
        continue
    # comma
    i += 1
print(score)
