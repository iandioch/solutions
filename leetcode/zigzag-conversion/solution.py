class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        c = []
        ind = 0
        while ind < len(s):
            currRow = []
            if len(c) % (numRows-1) == 0:
                for i in range(min(numRows, len(s)-ind)):
                    currRow.append(s[ind + i])
                ind += numRows
            else:
                empty = numRows - 1 - (len(c) % (numRows-1))
                currRow = ['']*empty + [s[ind]]
                currRow += [''] * (numRows - len(currRow))
                ind += 1
            c.append(currRow)
        ans = ''
        for r in range(numRows):
            for col in c:
                if r < len(col):
                    ans += col[r]
        return ans
