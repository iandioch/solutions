import sys
from collections import defaultdict

def self_similar(s, n):
    d = defaultdict(int)
    for i in range(len(s)-n+1):
        t = s[i:i+n]
        d[t] += 1


    for i in range(len(s)-n+1):
        t = s[i:i+n]
        if d[t] == 1:
            return False
    return True

def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        found = False
        for n in range(len(line)-1, 0, -1):
            if self_similar(line, n):
                print(n)
                found = True
                break

        if not found:
            print('0')

main()
