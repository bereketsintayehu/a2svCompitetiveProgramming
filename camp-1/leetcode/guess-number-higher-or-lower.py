# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 0, n + 1

        while l + 1 < h:
            mid = (l + h) // 2
            res = guess(mid)

            if not res:
                return mid

            if res > 0:
                l = mid
                
            else:
                h = mid

        return l
