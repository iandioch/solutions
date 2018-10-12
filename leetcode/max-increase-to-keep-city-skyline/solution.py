class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxv = [max(grid[i]) for i in range(len(grid))]
        maxh = [max(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        tot = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                c = grid[i][j]
                poss = min(maxv[i], maxh[j])
                tot += poss - c
        return tot
