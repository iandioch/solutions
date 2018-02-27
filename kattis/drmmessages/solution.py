ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rotate(t):
    val = sum(ALPHABET.find(c) for c in t)
    return ''.join(ALPHABET[(ALPHABET.find(c)+val)%len(ALPHABET)] for c in t)

s = input()
a, b = rotate(s[:len(s)//2]), rotate(s[len(s)//2:])
print(''.join(ALPHABET[(ALPHABET.find(c) + ALPHABET.find(d))%len(ALPHABET)] for c,d in zip(a,b)))
