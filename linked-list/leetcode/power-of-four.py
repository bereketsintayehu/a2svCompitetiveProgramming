class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def check(n):
            if n == 1:
                return True
            if n < 1:
                return False
                
            return check(n / 4)

        return check(n)