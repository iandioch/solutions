import sys

LIM = 2**31

var_values = {}


def overflow_or_underflow_val(x):
    while x < -LIM:
        x += LIM
    while x >= LIM:
        x -= LIM
    return x


def calc_with_overflow_underflow(x, op, y):
    #print('calcing {} {} {}'.format(x, op, y))
    if op == '/':
        return overflow_or_underflow_val(x//y)
    if op == '+':
        return overflow_or_underflow_val(x+y)
    if op == '-':
        return overflow_or_underflow_val(x-y)
    if op == '*':
        return overflow_or_underflow_val(x*y)

def eval_condition(x, op, y):
    #print('evaling condition {} {} {}'.format(x, op, y))
    a = get_val(x)
    b = get_val(y)
    if op == '=':
        return a == b
    if op == '>':
        return a > b
    if op == '<':
        return a < b
    if op == '<>':
        return a != b
    if op == '<=':
        return a <= b
    if op == '>=':
        return a >= b
        
def get_val(varname):
    #print('getting val of {}'.format(varname))
    if varname in var_values:
        return var_values[varname]
    return int(varname)

def get_print_val(v):
    if v[0][0] == '"':
        return ' '.join(v).strip('"')
    return var_values[v[0]]


line_parts = [s.split() for s in sys.stdin.readlines()]
label_parts = {p[0]:p for p in line_parts}
sorted_labels = sorted(label_parts.keys(), key=lambda s: int(s))
label_indices = {sorted_labels[i]:i for i in range(len(sorted_labels))}

curr_label = sorted_labels[0]

while True:
    parts = label_parts[curr_label]
    command = parts[1]
    if command == 'LET':
        varname = parts[2]
        _ = parts[3]
        ans = None
        if len(parts) == 5:
            ans = get_val(parts[4])
        else:
            ans = calc_with_overflow_underflow(get_val(parts[4]),
                                               parts[5],
                                               get_val(parts[6]));
        var_values[varname] = ans
        # let
        pass
    elif command == 'IF':
        x = parts[2]
        op = parts[3]
        y = parts[4]
        dest = parts[-1]
        if eval_condition(x, op, y):
            #print('condition true, jumping to', dest)
            curr_label = dest
            continue
    elif command == 'PRINT':
        sys.stdout.write(str(get_print_val(parts[2:])))
    elif command == 'PRINTLN':
        print(get_print_val(parts[2:]))
    curr_index = label_indices[curr_label]
    if curr_index == len(sorted_labels)-1:
        break
    curr_label = sorted_labels[curr_index+1]
