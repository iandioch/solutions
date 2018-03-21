def encrypt(s):
    t = []
    for c in s:
        a = 0
        if c != ' ':
            a = ord(c) - ord('a') + 1
        if len(t):
            t.append(t[-1] + a)
        else:
            t.append(a)

    u = []
    for c in t:
        c %= 27
        if c == 0:
            u.append(' ')
        else:
            u.append(chr(c + ord('a') - 1))
    return ''.join(u)

def decrypt(s):
    t = []
    tmp = 0
    for c in s:
        a = 0
        if c != ' ':
            a = ord(c) - ord('a') + 1
        a -= tmp
        while a < 0:
            a += 27
        tmp += a
        t.append(a)
    u = []
    for c in t:
        if c == 0:
            u.append(' ')
        else:
            u.append(chr(c + ord('a') - 1))
    return ''.join(u)

t = int(input())
for _ in range(t):
    s = input()
    op = s[0]
    s = s[2:]
    if op == 'e':
        print(encrypt(s))
    else:
        print(decrypt(s))
