class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = set(nums)
        for i in range(len(nums)+1):
            if i not in d:
                return i