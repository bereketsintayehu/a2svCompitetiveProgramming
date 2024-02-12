class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = list(accumulate(nums))
        ans = pre[-1]
        n = len(nums)
        m = 0

        for p in pre:
            ans = max(ans, p - m)
            m = min(m, p)

        return ans