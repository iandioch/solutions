import sys
from collections import deque

def custom_eval(inp):
    tot = inp[0]
    op = None
    for c in inp[1:]:
        if c in set(['+', '*']):
            op = c
        else:
            tot = eval('{} {} {}'.format(tot, op, c))
    return tot

def remove_bracket(inp):
    start = -1
    for i, item in enumerate(inp):
        if item == '(':
            start = i
    if start < 0:
        return inp, False
    tot = 0
    end = len(inp)
    for i in range(start, len(inp)):
        if inp[i] == ')':
            end = i
            break
    ans = custom_eval(inp[start + 1:end])
    return inp[:start] + [ans] + inp[end+1:], True

def main():
    ans = 0
    for line in sys.stdin.readlines():
        items = []
        for c in line.strip():
            if c == ' ':
                continue
            if c in '+*()':
                items.append(c)
            else:
                items.append(int(c))
        while len(items) > 1:
            items, made_step = remove_bracket(items)
            if not made_step:
                break
        ans += (custom_eval(items))
    print(ans)

main()
