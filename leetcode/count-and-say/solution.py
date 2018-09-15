class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(n-1):
            curr = s[0]
            n = 1
            d = []
            for i in range(1, len(s)):
                if s[i] == curr:
                    n += 1
                else:
                    d.append((curr, n))
                    curr = s[i]
                    n = 1
            d.append((curr, n))
            t = ''
            for e in d:
                t += str(e[1]) + str(e[0])
            s = t
        return s
