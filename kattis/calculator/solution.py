import sys

# operator precedence
ops = {
    '-': 1,
    '+': 1,
    '*': 2,
    '/': 2,
    '$': 3,
}

def compare(a, b):
    if a not in ops or b not in ops:
        return False
    return ops[a] <= ops[b]

for line in sys.stdin.readlines():
    line = line.strip().replace(' ','')
    d = []
    stack = []

    skip_until = -1 # Used to track multi-digit numbers
    prev = None # Used to find unary minus operator
    # convert to postfix
    for i in range(len(line)):
        if i < skip_until:
            continue
        c = line[i]
        if c == '-' and (prev in ops or prev == '(' or prev is None):
            stack.append('$') # unary -
        elif c in ops:
            while len(stack) and compare(c, stack[-1]):
                d.append(stack.pop())
            stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while len(stack) and stack[-1] != '(':
                d.append(stack.pop())
            stack.pop()
        else:
            # handle multiple digits
            s = c
            for j in range(i+1, len(line)):
                if line[j].isdigit():
                    s += line[j]
                    skip_until = j+1
                else:
                    break
            d.append(s)
        prev = c
    while len(stack):
        d.append(stack.pop())

    # evaluate posfix
    stack = []
    for c in d:
        if c.isdigit():
            stack.append(float(c))
        elif c == '$':
            stack.append(-stack.pop())
        else:
            a, b = stack.pop(), stack.pop()
            if c == '-':
                stack.append(b-a)
            elif c == '+':
                stack.append(a+b)
            elif c == '*':
                stack.append(b*a)
            else:
                stack.append(b/a)
    print('{:.2f}'.format(stack[0]))
