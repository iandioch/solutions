import sys

def fact(n):
    ans = 1;
    for i in xrange(2, n+1):
        ans *= i
    return ans

for line in sys.stdin.readlines():
    letter_counts = {}
    for letter in line[:-1]:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    ans = fact(len(line)-1)
    for letter in letter_counts:
        ans /= fact(letter_counts[letter])
    print(ans)
