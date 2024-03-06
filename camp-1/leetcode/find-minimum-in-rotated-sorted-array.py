class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        l, h = -1, len(nums)
        while l + 1 < h:
            mid = (l + h) // 2
            if nums[mid] < nums[-1]:
                h = mid
            else:
                l = mid
        
        return nums[h] if h < len(nums) else nums[-1]