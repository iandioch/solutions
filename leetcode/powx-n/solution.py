class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        tmp = self.myPow(x, n//2)
        if n % 2 == 0:
            return tmp * tmp
        else:
            return x * tmp * tmp
