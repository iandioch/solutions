s = input()
t = []
for i in range(len(s)//2):
    n = int(s[i*2:i*2+2], 16)
    t.append(n)


ans_k, ans_x = None, None
for k in range(256):
    for x in range(256):
        o = []
        b = k
        for e in t:
            o.append(e^b)
            b = (b + x) % 256
        f = ''.join(map(chr, o))
        if 'answer' in f:
            ans_k = k
            ans_x = x
            print(ans_k, ans_x)
            break

t = s[:]
while True:
    n = 0
    ok = set('qwertyuiopasdfghjklzxcvbnm "')
    restart = False
    b = ans_k
    o = []
    for i in range(len(t)//2):
        e = int(t[i*2:i*2+2], 16)
        c = e^b
        if c > 128:
            t = t[:i*2-1] + '0' + t[i*2-1:]
            f = ''.join(map(chr, o))

            restart = True
            break
        o.append(c)
        b = (b + ans_x) % 256
    if restart:
        continue
    f = ''.join(map(chr, o))
    print(f)
    break
