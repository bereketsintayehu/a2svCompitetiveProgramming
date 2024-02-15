class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        cnt = defaultdict(int)
        n = len(nums)

        ans = [0] * n

        for i in range(n):
            ans[i] += i * cnt[nums[i]] - d[nums[i]]

            cnt[nums[i]] += 1
            d[nums[i]] += i
        
        d = defaultdict(int)
        cnt = defaultdict(int)

        for i in range(n - 1, -1, -1):
            ans[i] += d[nums[i]] - i * cnt[nums[i]]

            cnt[nums[i]] += 1
            d[nums[i]] += i

        return ans