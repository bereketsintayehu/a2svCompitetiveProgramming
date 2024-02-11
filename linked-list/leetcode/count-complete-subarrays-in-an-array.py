class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        t = len(set(nums))
        n = len(nums)
        ans = 0

        for i in range(n):
            v = set()
            for j in range(i, n):
                v.add(nums[j])
                if len(v) == t:
                    ans += 1

        return ans



