class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = currSum = 0
        res = len(nums) + 1

        for r in range(len(nums)):
            currSum += nums[r]

            while currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1

        return res if res != len(nums) + 1 else 0