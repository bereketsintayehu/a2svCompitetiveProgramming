class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans, m = 0, nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > m:
                t = math.ceil(nums[i] / m)
                ans += t - 1
                m = nums[i] // t
            else:
                m = nums[i]

        return ans