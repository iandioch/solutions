import sys

lines = sys.stdin.readlines()

in_data = [int(x) for x in lines[0][:-1].split(',')]


possible_keys = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            possible_keys.append(a + b + c)


for key in possible_keys:
    curr = 0
    decrypt = ''
    for i in in_data:
        d = ord(key[curr])
        decrypt += chr(i ^ d)
        curr = (curr + 1) % len(key)
    if all(w in decrypt.lower() for w in ['of', 'the', 'and', ' ', '.', ',', 'it', 'is', 'not']):
        print decrypt
        print sum(ord(c) for c in decrypt)
