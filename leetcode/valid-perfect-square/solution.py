class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = self.mySqrt(num)
        return s*s == num
        
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0
        lo = 1
        hi = x
        ans = 0
        while lo < hi:
            mid = (lo + hi)//2
            sq = mid*mid
            if sq == x:
                return mid
            if sq < x:
                ans = mid
                lo = mid + 1
            else:
                hi = mid
        return ans
