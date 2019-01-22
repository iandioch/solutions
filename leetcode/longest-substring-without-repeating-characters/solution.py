class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        visited = defaultdict(lambda: -1)
        
        curr_len = 0
        max_len = 0
        
        for i, c in enumerate(s):
            prev = visited[c]
            if prev == -1 or (i - curr_len > prev):
                curr_len += 1
            else:
                if curr_len > max_len:
                    max_len = curr_len
                curr_len = i - prev
            visited[c] = i
        if curr_len > max_len:
            max_len = curr_len
        return max_len
