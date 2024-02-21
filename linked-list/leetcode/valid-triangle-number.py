class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()
        ans = 0

        for i in range(n - 2):
            l = i + 1
            for r in range(i + 2, n):
                while l < r and nums[i] + nums[l] <= nums[r]:
                    l += 1
                ans += r - l

        return ans