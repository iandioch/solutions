import crypt

from hmac import compare_digest as compare_hash
from itertools import product

ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXXYZ'
HASH = 'dXWxIS6i6irN6'
SALT = HASH[0:2]

found = False
repeat = 1
while not found:
    for pw in product(ALPHABET, repeat=repeat):
        pw = ''.join(pw)
        found = compare_hash(crypt.crypt(pw, SALT), HASH) 
        if found:
            print(pw)
            break
    repeat += 1
