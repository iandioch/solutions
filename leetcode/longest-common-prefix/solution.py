class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ""
        i = 0
        if not len(strs):
            return ""
        while True:
            if i >= len(strs[0]):
                break
            c = strs[0][i]
            ok = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    ok = False
                    break
                if strs[j][i] != c:
                    ok = False
                    break
            if ok:
                s += c
                i += 1
            else:
                break
        return s
