class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) 
        
        while l<r:
            if nums[l] == 0:
                nums.pop(l)
                nums.append(0)
                r -= 1
            else:
                l += 1
            
        