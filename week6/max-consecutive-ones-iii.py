class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = longest = 0
        freq_map = {1:0, 0:0}

        for r in range(len(nums)):
            freq_map[nums[r]] += 1

            while freq_map[0] > k:
                freq_map[nums[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest