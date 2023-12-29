class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        return sum([n - i - 1 for i in range(n - 1) if nums[i] != nums[i + 1]])