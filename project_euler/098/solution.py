import sys

def replace_letters(s, d):
    return ''.join(d[c] for c in s)

def map_to_sig(s):
    l = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    d = {}
    for c in s:
        if c not in d:
            d[c] = l[i]
            i += 1    
    return replace_letters(s, d), d

def get_anagrams(l):
    anagrams = {} 
    for s in l:
        a = ''.join(sorted(str(s)))
        if a in anagrams:
            anagrams[a].append(s)
        else:
            anagrams[a] = [s] 
    return anagrams

def get_pairs(d):
    pairs = []
    for s in d.keys():
        if len(d[s]) == 1:
            continue
        a = d[s]
        for i in xrange(0, len(a) - 1):
            for j in xrange(i+1, len(a)):
                pairs.append((a[i], a[j]))   
                pairs.append((a[j], a[i]))

    return pairs

squares = set()

for i in xrange(1, 1000):
    squares.add(i*i)

word_file = ''.join(sys.stdin.readlines())
words = [s.strip()[1:-1] for s in word_file.split(",")]

anagrams = get_anagrams(words)
word_pairs = get_pairs(anagrams)

num_anagrams = get_anagrams(squares)
num_pairs = get_pairs(num_anagrams)
    
largest = 0

for w in word_pairs:
    wa, d = map_to_sig(w[0])
    wb = replace_letters(w[1], d)
    for n in num_pairs:
        if len(w[0]) != len(str(n[0])):
            continue
        na, e = map_to_sig(str(n[0]))
        nb = replace_letters(str(n[1]), e)
        if wa == na and wb == nb:
            largest = max(largest, n[0], n[1])

print largest
        
