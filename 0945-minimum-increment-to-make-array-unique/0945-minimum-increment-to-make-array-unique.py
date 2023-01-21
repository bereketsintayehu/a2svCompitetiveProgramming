class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        opCount = 0
        nextNum = 0
        nums.sort()
        for i in nums:
            opCount += max(nextNum - i, 0)
            nextNum = max(nextNum, i) + 1
        return opCount