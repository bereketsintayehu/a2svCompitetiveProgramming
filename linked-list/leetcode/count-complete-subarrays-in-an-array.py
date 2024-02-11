class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        if not nums:
            return 1

        t = len(set(nums))
        n = len(nums)
        ans = 0
        start = 0
        count = Counter()
        

        for end in range(n):
            count[nums[end]] += 1

            while len(count) == t:
                ans += n - end

                count[nums[start]] -= 1
                if not count[nums[start]]:
                    del count[nums[start]]

                start += 1
        
        return ans



