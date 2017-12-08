import sys
from collections import defaultdict

reg = defaultdict(int)
highest_value = 0

def check_op(check_reg, check, v):
    val = reg[check_reg]
    if check == '>':
        return val > v
    if check == '<':
        return val < v
    if check == '==':
        return val == v
    if check == '>=':
        return val >= v
    if check == '<=':
        return val <= v
    if check == '!=':
        return val != v
    print('Do not recognise comparator', check)
    return False

for line in sys.stdin.readlines():
    parts = line.split()
    mod_reg = parts[0]
    op = parts[1]
    operand = int(parts[2])
    check_reg = parts[4]
    check = parts[5]
    check_operand = int(parts[6])
    if check_op(check_reg, check, check_operand):
        if op == 'inc':
            reg[mod_reg] += operand
        elif op == 'dec':
            reg[mod_reg] -= operand
        else:
            print('Do not recongise operator', op)
        highest_value = max(highest_value, reg[mod_reg])

print(highest_value)
