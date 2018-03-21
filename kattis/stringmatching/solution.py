import sys

# Knuth-Morris-Pratt

def kmp_table(w):
    cnd = 0
    t = [-1]
    for pos in range(1, len(w)):
        if w[pos] == w[cnd]:
            t.append(t[cnd])
            cnd += 1
        else:
            t.append(cnd)
            cnd = t[cnd]
            while cnd >= 0 and w[pos] != w[cnd]:
                cnd = t[cnd]
            cnd += 1
    t.append(cnd)
    return t

def kmp(s, w):
    t = kmp_table(w)
    j, k = 0, 0
    np = 0
    while j < len(s):
        if w[k] == s[j]:
            j += 1
            k += 1
            if k == len(w):
                # Found an occurance
                yield j-k
                np += 1
                k = t[k]
        else:
            k = t[k]
            if k < 0:
                j += 1
                k += 1

lines = sys.stdin.readlines()
for i in range(0, len(lines), 2):
    print(' '.join(str(a) for a in kmp(lines[i+1].strip(), lines[i].strip())))
