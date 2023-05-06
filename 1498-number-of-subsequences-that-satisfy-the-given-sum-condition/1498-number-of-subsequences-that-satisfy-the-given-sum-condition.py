class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        kMod = 1_000_000_007
        count = 0
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                count += pow(2, right - left, kMod) 
                left += 1
            else:
                right -= 1
        
        return count % kMod