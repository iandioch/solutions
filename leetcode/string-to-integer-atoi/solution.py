class Solution:
    def myAtoi(self, s: str) -> int:
        n = 0
        s = s.lstrip()
        if not len(s):
            return 0
        i = 0
        neg = False
        if s[0] == '-':
            neg = True
            i = 1
        elif s[0] == '+':
            i = 1
        for c in s[i:]:
            if c not in '0123456789':
                break
            n *= 10
            n += ord(c) - ord('0')
        if neg:
            n *= -1
            
        n = max(-2**31, min(n, 2**31 - 1))
        return n
