class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        x = [1] * n
        y = [1] * n
        
        for i in range(1, n):
            x[i] = x[i-1] * nums[i-1]
        for i in range(n - 2, -1, -1):
            y[i] = y[i+1] * nums[i+1]
        return [x[i] * y[i] for i in range(n)]
        