class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = s.split()
        if not len(t):
            return 0
        return len(t[-1])
