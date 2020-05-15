import sys

def longest_repeating_substring(s):
    n = len(s)
    memo = [[0 for x in range(n+1)] for y in range(n+1)]
    index = 0
    best = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if (s[i-1] == s[j-1] and memo[i-1][j-1] < (j-i)):
                    memo[i][j] = memo[i-1][j-1] + 1
                    if memo[i][j] > best:
                        best = memo[i][j]
                        index = max(i, index)
            else:
                memo[i][j] = 0
    return s[index-best:index]

def main():
    s = ''.join(sys.stdin.readlines())
    print(longest_repeating_substring(s))

main()
