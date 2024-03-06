class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        while l <= h:
            mid = (l + h) // 2
            if mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                h = mid -1
            else:
                return mid
            
        return h