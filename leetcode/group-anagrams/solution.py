class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        d = defaultdict(list)
        for s in strs:
            d[str(sorted(s))].append(s)
        return [d[e] for e in d]
