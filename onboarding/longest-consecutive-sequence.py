class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
    
        for num in nums:
            if num - 1 not in s:
                curr = 0
                while num + curr in s:
                    curr += 1
                    
                ans = max(ans, curr)
                
        return ans
