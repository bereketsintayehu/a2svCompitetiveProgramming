class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        MOD = 10 ** 9 + 7
        ans = 0
        n = bisect_right(nums, target)
        for i in range(n):
            j = bisect_right(nums, target - nums[i]) - 1
            if i <= j:
                ans += pow(2, j - i, MOD)

        return ans % MOD