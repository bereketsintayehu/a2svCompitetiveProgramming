class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max = nums[0] + nums[len(nums)-1]
        for i in range(1, len(nums)//2):
            if nums[i] + nums[-1-i] > max:
                max = nums[i] + nums[-1-i]
        return max
            
        