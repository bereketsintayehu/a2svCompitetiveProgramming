class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2]+nums[i-1]+nums[i]

        return ans