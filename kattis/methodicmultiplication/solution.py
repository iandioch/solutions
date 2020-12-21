def parse_peano(s):
    if s == '0':
        return 0
    return s.count('S')

def emit_peano(n):
    if n == 0:
        return '0'
    s = []
    for i in range(n):
        s.append('S(')
    s.append('0')
    for i in range(n):
        s.append(')')
    return ''.join(s)


a = parse_peano(input())
b = parse_peano(input())
print(emit_peano(a*b))
