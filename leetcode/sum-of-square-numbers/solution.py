class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        i = 0
        while i*i <= c:
            squares.add(i*i)
            i += 1
        for n in squares:
            if (c - n) in squares:
                return True
        return False
