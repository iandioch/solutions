class Solution:
    def romanToInt(self, s: str) -> int:
        d = [
            ('IV', 4),
            ('IX', 9),
            ('XL', 40),
            ('XC', 90),
            ('CD', 400),
            ('CM', 900),
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ]
        ans = 0
        while len(s):
            for c in d:
                if s.startswith(c[0]):
                    ans += c[1]
                    s = s[len(c[0]):]
                    break
        return ans
