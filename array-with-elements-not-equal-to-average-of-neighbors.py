class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums), 2):
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
        return nums
            
        
