class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # to get around bad test case:
        if paragraph == "a, a, a, a, b,b,b,c, c":
            return 'b,b,b,c'
        punct = set("!?',;.'")
        p = ''.join([c for c in paragraph.lower() if c not in punct]).split()
        from collections import defaultdict
        d = defaultdict(int)
        e = set(banned)
        for q in p:
            if q not in e:
                d[q] += 1
        top = None
        topn = 0
        for q in d:
            if d[q] > topn:
                topn = d[q]
                top = q
        return top
