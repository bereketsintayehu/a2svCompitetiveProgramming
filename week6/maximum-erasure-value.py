class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        windowStart = 0
        curr = 0

        for windowEnd in range(len(nums)):
            curr += nums[windowEnd]
            freq[nums[windowEnd]] += 1

            while freq[nums[windowEnd]] > 1:
                curr -= nums[windowStart]
                freq[nums[windowStart]] -= 1

                if freq[nums[windowStart]] == 0:
                    del freq[nums[windowStart]]
                    
                windowStart += 1
 
            ans = max(ans, curr)

        return ans