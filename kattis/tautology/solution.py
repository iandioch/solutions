from itertools import product
varnames = {
        'p': 0,
        'q': 1,
        'r': 2,
        's': 3,
        't': 4
}

def test(wff, vals):
    # returns result, remain, where result is a value and remain is the rest of the unparsed string
    now = wff[0]
    if now in varnames:
        return vals[varnames[now]], wff[1:]
    elif now == 'N':
        ans, rem = test(wff[1:], vals)
        return not ans, rem
    elif now == 'K':
        a, second = test(wff[1:], vals)
        b, remain = test(second, vals)
        return a and b, remain
    elif now == 'A':
        a, second = test(wff[1:], vals)
        b, remain = test(second, vals)
        return a or b, remain
    elif now == 'C':
        a, second = test(wff[1:], vals)
        b, remain = test(second, vals)
        return (not a) or b, remain
    elif now == 'E':
        a, second = test(wff[1:], vals)
        b, remain = test(second, vals)
        return a == b, remain

while True:
    s = input()
    if s == '0':
        break
    ok = True
    for vals in product([True, False], repeat=5):
        ok = ok and test(s, vals)[0]
    print('tautology' if ok else 'not')
