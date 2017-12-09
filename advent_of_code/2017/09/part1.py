i = 0
s = input()
junk = False
stack = []
score = 0
while i < len(s):
    if s[i] == '!':
        i += 2
        continue
    if junk:
        if s[i] == '>':
            junk = False
        i += 1
        continue
    if s[i] == '<':
        junk = True
        i += 1
        continue
    if s[i] == '{':
        stack.append(i)
        i += 1
        continue
    if s[i] == '}':
        score += len(stack)
        stack.pop()
        i += 1
        continue
    # comma
    i += 1
print(score)
