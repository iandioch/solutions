class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = set('abcdefghijklmnopqrstuvwxyz0123456789')
        t = [c for c in s.lower() if c in a]
        return t == t[::-1]
