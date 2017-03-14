import sys

vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])

for line in sys.stdin.readlines():
    out = []
    for word in line.split():
        if word[0] in vowels:
            out.append(word + 'yay')
        else:
            i = 0
            while i < len(word):
                if word[i] in vowels:
                    break
                i += 1
            out.append(word[i:] + word[:i] + 'ay')
    print(' '.join(out))
