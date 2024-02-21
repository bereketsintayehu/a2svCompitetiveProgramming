class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0

        for i in range(len(nums) - 1):
            curr -= 1
            curr = max(curr, nums[i])
            if not curr:
                return False
        
        return True