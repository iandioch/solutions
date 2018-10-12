class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        tot = cost + [0]
        for i in range(2, len(tot)):
            tot[i] += min(tot[i-1], tot[i-2])
        return tot[-1]
