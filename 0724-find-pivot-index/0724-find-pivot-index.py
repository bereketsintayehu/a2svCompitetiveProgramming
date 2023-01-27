class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = [nums[0]]
        for i in range(1, len(nums)):
            preSum.append(nums[i]+preSum[i-1])
        if preSum[-1] - preSum[0] == 0:
            return 0
        for i in range(1, len(nums)):
            if preSum[-1] - preSum[i] == preSum[i-1]:
                return i
        return -1
        
        