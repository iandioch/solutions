class Solution:

    def prettify(self, b, n):
        d = []
        for row in b:
            d.append('.'*row + 'Q' + '.'*(n - row - 1))
        return d

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []

        def recurse(board):
            # board = list describing position of queen in each row
            if len(board) == n:
                # we're done
                ans.append(self.prettify(board, n))
            else:
                j = len(board)
                for i in range(n):
                    ok = True
                    for k in range(len(board)):
                        if board[k] == i or (abs(board[k] - i) == abs(k - len(board))):
                            ok = False
                            break
                    if ok:
                        recurse(board + [i])
        recurse([])            
        return ans
