class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        bestn = 1
        best = s[0]
        n = len(s)
        for mid in range(n):
            w = 0
            maxn = 1
            while True:
                w += 1
                if mid - w < 0 or mid + w >= n:
                    break
                if s[mid-w] != s[mid+w]:
                    break
                maxn += 2
            if maxn > bestn:
                bestn = maxn
                best = s[mid-w+1:mid+w]
        for left in range(n-1):
            if s[left] != s[left+1]:
                continue
            w = 0
            maxn = 2
            while True:
                w += 1
                if left - w < 0 or left + 1 + w >= n:
                    break
                if s[left-w] != s[left+1+w]:
                    break
                maxn += 2
            if maxn > bestn:
                bestn = maxn
                best = s[left-w+1:left+w+1]
        return best
