class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        curr = 0

        for i, num in enumerate(nums):
            curr += num
            avg = ceil(curr / (i + 1))
            ans = max(ans, avg)

        return ans