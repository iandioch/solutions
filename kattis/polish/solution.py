import sys

ops = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
}

digs = set('-0123456789')

def is_oppable(s):
    return all(c in digs for c in s)

def polish(expr, index):
    if expr[index] not in ops:
        return expr[index], index+1
    op = expr[index]
    arg0, next_index = polish(expr, index+1)
    arg1, next_index = polish(expr, next_index)
    if is_oppable(arg0) and is_oppable(arg1):
        return str(ops[op](int(arg0), int(arg1))), next_index
    return ' '.join((op, arg0, arg1)), next_index

curr = 1
for line in sys.stdin.readlines():
    parts = line.strip().split()
    ans, _ = polish(parts, 0)

    print('Case {}: {}'.format(curr, ans))
    curr += 1
