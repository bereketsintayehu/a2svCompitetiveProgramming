class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        return pow(x, n - 1) * x