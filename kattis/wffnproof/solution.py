while True:
    s = input()
    if s == '0':
        break
    var = set('pqrst')
    unary = set('N')
    binary = set('KACE')
    tokens = [c for c in s if c in var]
    ops = [c for c in s if c in binary]
    ns = [c for c in s if c in unary]
    while True:
        if len(ops) == 0:
            break
        if len(tokens) <= 1:
            break
        tokens.sort(key = len)
        a = tokens.pop()
        b = tokens.pop()
        op = ops.pop()
        tokens.append(op + a + b)

    if len(tokens) == 0:
        print('no WFF possible')
        continue
    tokens.sort(key = len)
    for _ in range(len(ns)):
        tokens[-1] = 'N' + tokens[-1]
    print(tokens[-1])
